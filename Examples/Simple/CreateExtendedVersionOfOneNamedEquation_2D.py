import os, sys, inspect

# ensure pyeq3 can be imported
if -1 != sys.path[0].find('pyeq3-master'):raise Exception('Please rename git checkout directory from "pyeq3-master" to "pyeq3"')
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq3IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq3IimportDirectory not in sys.path:
    sys.path.append(pyeq3IimportDirectory)
    
import pyeq3


# print all possible extended version names
print("List of all possible extended version names")
for extendedVersionName in pyeq3.ExtendedVersionHandlers.extendedVersionHandlerNameList:
    print(extendedVersionName)
    
print()

# create an extended version of one equation
equation = pyeq3.Models_2D.BioScience.HyperbolicLogistic('SSQABS', 'InverseWithOffset')

# note that the extended version name can contain spaces
equation = pyeq3.Models_2D.BioScience.HyperbolicLogistic('SSQABS', 'Inverse With Offset')

print("Instantiated", equation.GetDisplayName())

print()

#print("This should raise an exception")
#equation = pyeq3.Models_2D.BioScience.HyperbolicLogistic('SSQABS', 'Bad Extended Version Name')