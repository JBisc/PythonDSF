import pythondcs

t = pythondcs.PythonDCS();
versionstring = t.gCode("M115")

print("Get version string:")
print(versionstring)

print("Choose File writing")
print(t.gCode("M28 \"Test.gcode\" "))
print("Write file on the raspberry onto the Duet")
fh = open("../gcode/example.gcode", "r")
print(t.gCode(fh.read()))

print("Close File writing")
print(t.gCode("M29"))

print("Show all files")
print(t.gCode("M20 S1"))




