from pathlib import Path

#This module relates to the pathlib found here: https://docs.python.org/3/library/pathlib.html#module-pathlib
# Absolute path (example):
# c:\Program Files\Microsoft
#
# Relative path:
path = Path("LearningTheBasics") #Set current directory as Default without any given arguments
path.exists() #Boolean - True/False on if it exists
#path.mkdir() #Creates new directory at given path (object)
#path.rmdir() #Removes directory at given path (object)
for file in path.glob('*.py'): #Generates a generator object with all the .py-files found in the given path (object)
    print(file)
