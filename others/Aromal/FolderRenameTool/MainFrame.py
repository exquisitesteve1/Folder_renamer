import os
import numpy as np
import Fn_Def as rf
from colorama import init
init()
from colorama import Fore

# basedir = "D:/LEGACY"
# print(type(basedir))
fileName = "RenameData_CD.txt"

print(Fore.YELLOW+"Process Type : 1 - Refresh | 2 - Rename | 3 - Exit\n")
flag = input("Enter Type Num: ")

if(flag == "1"):
    rf.Refresh_Folder(("D:/DataConversion/QA/Scripts/TestingScripts/ValidationScripts/LEGACY/02.Scripts/CD"), fileName)

if(flag == "2"):
    renameRow = np.loadtxt(fileName, dtype="str")
    arrayLen = len(renameRow)
    folderCount = rf.Folder_Count(("D:/DataConversion/QA/Scripts/TestingScripts/ValidationScripts/LEGACY/01.Functions/CD"))

    if arrayLen == folderCount:
        rf.Rename_Folder(("D:/DataConversion/QA/Scripts/TestingScripts/ValidationScripts/LEGACY/01.Functions/CD"), fileName, renameRow)
    else:
        print(Fore.RED+"!!!fatal error: number of folders being modified does not match the number of folders present in functions folder!!!")

    folderCount = rf.Folder_Count(("D:/DataConversion/QA/Scripts/TestingScripts/ValidationScripts/LEGACY/02.Scripts/CD"))

    if arrayLen == folderCount:
        rf.Rename_Folder(("D:/DataConversion/QA/Scripts/TestingScripts/ValidationScripts/LEGACY/02.Scripts/CD"), fileName, renameRow)
    else:
        print(Fore.RED+"!!!fatal error: number of folders being modified does not match the number of folders present in scripts folder!!!")  

if(flag == "3"):
    print(Fore.GREEN+"Exited Successfully")
    exit(0)