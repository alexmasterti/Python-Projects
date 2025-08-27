import os
currentDirectoryPath = os.getcwd()
print(currentDirectoryPath)
listofFileNames = os.listdir(currentDirectoryPath)
for name in listofFileNames:
    if ".py" in name:
        print(name)
