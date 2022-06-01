import os
from colorama import init
init()
from colorama import Fore

def Refresh_Folder(basedir, fileName):
    #removing all the present folder names in the txt file
    f = open(fileName, "r+")
    f.truncate()
    f.close()

    #inserting currently present foldernames in the txt file   
    f = open(fileName, "a")
    for fn in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, fn)):
            continue
        else:
            f.write(str(fn)+'\n')

    # #Removing trailing lines from the text file
    # readFile = open("RenameData_OD.txt")
    # lines = readFile.readlines()
    # readFile.close()

    # w = open("RenameData_OD.txt",'w')
    # w.writelines([item for item in lines[:-1]])
    # w.close()

    print(Fore.GREEN+"File refresh successfully completed")
    
def Rename_Folder(basedir, fileName, renameRow):
    #renaming all the folders present in accordance with the names in txt file
    i = 0
    for fn in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, fn)):
            continue
        if fn != renameRow[i]:
            os.rename(os.path.join(basedir, fn),os.path.join(basedir,renameRow[i]))
            print(Fore.GREEN+"Successfully renamed " + fn + " to " + renameRow[i])
            i = i + 1
        if fn == renameRow[i]:
            i = i + 1

def Folder_Count(basedir):
    folderCount = 0

    for fn in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, fn)):
            continue
        else:
            folderCount = folderCount + 1
    
    return folderCount    