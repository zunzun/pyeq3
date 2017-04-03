import os, sys, dispy

# ensure pyeq3 can be imported
if -1 != sys.path[0].find('pyeq3-master'):raise Exception('Please rename git checkout directory from "pyeq3-master" to "pyeq3"')
importDir =  os.path.join(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '..'), '..')
if importDir not in sys.path:
    sys.path.append(importDir)
    
import pyeq3



# this is the function to be run on the cluster
def fitEquationUsingDispyCluster(inEquationString, inFittingTargetString, inExtendedVersionString, inTextData):
	
    # individual cluster nodes must be able to import pyeq3
    import pyeq3

    equation = eval(inEquationString +'("' + inFittingTargetString + '", "' + inExtendedVersionString + '")')
    pyeq3.dataConvertorService().ConvertAndSortColumnarASCII(inTextData, equation, False)
    equation.Solve()
    fittedTarget = equation.CalculateAllDataFittingTarget(equation.solvedCoefficients)
   
    # this result list allows easy sorting of multiple results later
    return [fittedTarget, inEquationString, equation.solvedCoefficients]


equationString = 'pyeq3.Models_2D.Polynomial.Linear'

# see the pyeq3.IModel.fittingTargetDictionary
fittingTargetString = 'SSQABS'

textData = '''
1.0   1.1
2.0   2.2
3.0   3.4159  # Raspberry Pi humor
'''


jobCount = 20
print()
print('Creating dispy JobCluster')
cluster = dispy.JobCluster(fitEquationUsingDispyCluster)

print('Submitting', jobCount, 'jobs to the cluster')
jobs = []
for i in range(jobCount):
    job = cluster.submit(equationString, fittingTargetString, 'Default', textData)
    job.id = i # associate an ID to identify jobs (if needed later)
    jobs.append(job)

print('Waiting on jobs to complete  and collecting results')
for job in jobs:
    print()
    results = job()
    if job.exception: # can also use job.status
        print('Remote Exception in job number', job.id, '\n', str(job.exception))
    else:
        equation = eval(results[1] + '("' + fittingTargetString + '")')
        print('Success from job number', job.id)

print()
print('Done.')