



import os, sys, inspect

# ensure pyeq3 can be imported
if -1 != sys.path[0].find('pyeq3-master'):raise Exception('Please rename git checkout directory from "pyeq3-master" to "pyeq3"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq3IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq3IimportDirectory not in sys.path:
    sys.path.append(pyeq3IimportDirectory)
    
import pyeq3


functionString = 'm*X+B * (3/2)'

# note that the constructor is passed the function string here
equation = pyeq3.Models_2D.UserDefinedFunction.UserDefinedFunction(inUserFunctionString = functionString)

pyeq3.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)

equation.Solve()


##########################################################


print(equation.GetDisplayName(), str(equation.GetDimensionality()) + "D")
print('User Defined Function:', functionString)
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
print("Fitted Parameters:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))
