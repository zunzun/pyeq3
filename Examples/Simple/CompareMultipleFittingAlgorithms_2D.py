import os, sys, inspect

# ensure pyeq3 can be imported
if -1 != sys.path[0].find('pyeq3-master'):raise Exception('Please rename git checkout directory from "pyeq3-master" to "pyeq3"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq3IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq3IimportDirectory not in sys.path:
    sys.path.append(pyeq3IimportDirectory)
    
import pyeq3

fittingTargetText = 'SSQABS'

deEstimatedCoefficients = []

print('It is very rare for an algorithm to fit better than Levenberg-Marquardt,')
print('This example shows how to construct a test to determine if this is true.')
print()

for fittingAlgorithmName in pyeq3.solverService.ListOfNonLinearSolverAlgorithmNames:
    equation = pyeq3.Models_2D.BioScience.AphidPopulationGrowth(fittingTargetText, 'Offset')
    

    if equation.CanLinearSolverBeUsedForSSQABS() == True and fittingTargetText == 'SSQABS':
        raise Exception('The selected combination of equation and SSQABS fitting target does not use a non-linear solver')
    
    if fittingTargetText == 'ODR':
        raise Exception('ODR cannot use multiple fitting algorithms')        

    
    pyeq3.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)
    
    equation.deEstimatedCoefficients = deEstimatedCoefficients
    equation.Solve(inNonLinearSolverAlgorithmName=fittingAlgorithmName)
    deEstimatedCoefficients = equation.deEstimatedCoefficients # no need to re-run genetic algorithm
    
    print(fittingTargetText, 'of', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients), 'for the fitting algorithm', fittingAlgorithmName)
    print('Coefficients:', equation.solvedCoefficients)
    ()
    sys.stdout.flush()