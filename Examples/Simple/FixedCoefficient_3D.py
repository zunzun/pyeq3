import os, sys, inspect

# ensure pyeq3 can be imported
if -1 != sys.path[0].find('pyeq3-master'):raise Exception('Please rename git checkout directory from "pyeq3-master" to "pyeq3"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq3IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq3IimportDirectory not in sys.path:
    sys.path.append(pyeq3IimportDirectory)
    
import pyeq3


# see IModel.fittingTargetDictionary
equation = pyeq3.Models_3D.BioScience.HighLowAffinityIsotopeDisplacement('SSQABS')

pyeq3.dataConvertorService().ConvertAndSortColumnarASCII(equation.exampleData, equation, False)


# Note that only one coefficient is set to a fixed value in this
# example, using None for coefficients that are not fixed
equation.fixedCoefficients = [2.0, None]


equation.Solve()


##########################################################


print(equation.GetDisplayName(), str(equation.GetDimensionality()) + "D")
print(equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))
print("Fitted Parameters:")
for i in range(len(equation.solvedCoefficients)):
    print("    %s = %-.16E" % (equation.GetCoefficientDesignators()[i], equation.solvedCoefficients[i]))