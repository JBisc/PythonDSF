import pythondcs

t = pythondcs.PythonDCS();
versionstring = t.gCode("M115")

print("Get version string:")
print(versionstring)

print("Choose File writing")
print(t.gCode("M28 \"Test.gcode\" "))
print("Write followong commands in file")
print(t.gCode("G1 \n G1"))

print("Close File writing")
print(t.gCode("M29"))

print("Show all files")
print(t.gCode("M20 S1"))


#M28 "0:/gcodes/Filename.gco"

