import os, sys, inspect

# ensure pyeq3 can be imported
if -1 != sys.path[0].find('pyeq3-master'):raise Exception('Please rename git checkout directory from "pyeq3-master" to "pyeq3"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq3IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq3IimportDirectory not in sys.path:
    sys.path.append(pyeq3IimportDirectory)
    
import pyeq3


# named equations only
for modelsTypeName in ['Models_2D', 'Models_3D']:
    modelsFile = open(modelsTypeName + ".js", 'wt')
    models = eval('pyeq3.' + modelsTypeName)
    for submodule in inspect.getmembers(models):
        if inspect.ismodule(submodule[1]):

            moduleName = submodule[0].split('.')[-1]
            modelsFile.write('\nexports.' + moduleName + ' = module.exports.' + moduleName + ' = {};\n\n')
            
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    
                    # ignore these special classes
                    if equationClass[1].splineFlag or \
                       equationClass[1].userSelectablePolynomialFlag or \
                       equationClass[1].userCustomizablePolynomialFlag or \
                       equationClass[1].userSelectablePolyfunctionalFlag or \
                       equationClass[1].userSelectableRationalFlag or \
                       equationClass[1].userDefinedFunctionFlag:
                        continue
                                            
                    for extendedVersionString in ['Default', 'Offset']:
                        
                        if (extendedVersionString == 'Offset') and (equationClass[1].autoGenerateOffsetForm == False):
                            continue
                        
                        equationInstance = equationClass[1]('SSQABS', extendedVersionString)
                        className = equationInstance.__class__.__name__
                        if (extendedVersionString == 'Offset'):
                            className += '_WithOffset'
                        modelsFile.write('exports.' + moduleName + "." + className + ' = module.exports.' + moduleName + "." + className + ''' = {
    pythonModuleName : "''' + moduleName + '''",
    pythonClassName : "''' + equationClass[0] + '''",
    extendedVersionString : "''' + extendedVersionString + '''",
    displayName : "''' + equationInstance.GetDisplayName() + '''",
    displayHTML : "''' + equationInstance.GetDisplayHTML() + '''",
    dimensionality : ''' + str(equationInstance.GetDimensionality()) + ''',
    numberOfParameters : ''' + str(len(equationInstance.GetCoefficientDesignators())) + '''
};

''')