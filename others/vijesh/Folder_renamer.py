#from fileinput import filename
import xlrd
import os
ExcelPath= "D:\\Training\\TestOpenpyxl.xlsx"
workbook = xlrd.open_workbook(ExcelPath)
excel_Sheet=workbook.sheet_by_index(0)
fileName={}

for i in range(1,6):
   oldfilename=excel_Sheet.cell_value(i,0)
   fileName[oldfilename]=excel_Sheet.cell_value(i,1)
list_oldNames=list(fileName.keys())
#print(list_oldNames)
os.chdir('D:\\FolderRename')
#print(os.getcwd())
renamed_files=list(os.listdir())
#print(renamed_files)
for f in os.listdir():
   if str(f) in list_oldNames:
      if str(fileName[f]) not in renamed_files:
         os.rename(f,str(fileName[f]))
      else:
         print("file Name Duplication for {}".format(str(f)))
   else:
      pass
print("Files Renaming finished.....")