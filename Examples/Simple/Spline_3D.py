import os, sys, inspect

# ensure pyeq3 can be imported
if -1 != sys.path[0].find('pyeq3-master'):raise Exception('Please rename git checkout directory from "pyeq3-master" to "pyeq3"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq3IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq3IimportDirectory not in sys.path:
    sys.path.append(pyeq3IimportDirectory)
    
import pyeq3


# parameters are smoothing, xOrder, yOrder
equation = pyeq3.Models_3D.Spline.Spline(1.0, 3, 3) # cubic 3D spline

data = equation.exampleData

pyeq3.dataConvertorService().ConvertAndSortColumnarASCII(data, equation, False)
equation.Solve()


##########################################################


print("Equation:", equation.GetDisplayName(), str(equation.GetDimensionality()) + "D")
print("Fitting target of", equation.fittingTargetDictionary[equation.fittingTarget], '=', equation.CalculateAllDataFittingTarget(equation.solvedCoefficients))

print()

# at present, only these four languages are supported for spline-specific code
print(pyeq3.outputSourceCodeService().GetOutputSourceCodeCPP(equation))
#print(pyeq3.outputSourceCodeService().GetOutputSourceCodePYTHON(equation))
#print(pyeq3.outputSourceCodeService().GetOutputSourceCodeJAVA(equation))
#print(pyeq3.outputSourceCodeService().GetOutputSourceCodeJAVASCRIPT(equation))