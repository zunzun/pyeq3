



import os, sys, inspect

# ensure pyeq3 can be imported
if -1 != sys.path[0].find('pyeq3-master'):raise Exception('Please rename git checkout directory from "pyeq3-master" to "pyeq3"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq3IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq3IimportDirectory not in sys.path:
    sys.path.append(pyeq3IimportDirectory)
    
import pyeq3


# see IModel.fittingTargetDictionary
equation = pyeq3.Models_2D.BioScience.HyperbolicLogistic('SSQABS')

data = '''
  X        Y
5.357    10.376
5.457    10.489
5.797    10.874
5.936    11.049
6.161    11.327
6.697    12.054
6.731    12.077
6.775    12.138
8.442    14.744
9.769    17.068
9.861    17.104
'''
pyeq3.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
equation.Solve()


##########################################################


print(equation.GetDisplayName(), str(equation.GetDimensionality()) + "D")
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
print("Fitted Parameters:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
