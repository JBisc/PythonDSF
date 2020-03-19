#
# Just a short example how to use PythonDSF
#
import pythondcs

testInstance = pythondcs.PythonDCS();
versionstring = testInstance.gCode("M115")

print(versionstring)