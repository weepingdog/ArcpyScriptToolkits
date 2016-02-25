import os
import arcpy
from arcpy import env
import time
inputGDB = r"C:\Users\zhx\Desktop\321112DNT.gdb"
inputFrame = r"C:\Users\zhx\Desktop\T.gdb\F50000"
splitField = r"TID"
outputDir = r"D:\OUTPUT"

def Do(inputGDB,inputFrame,splitField,outputDir)
env.workspace = inputGDB
inputFCs = arcpy.ListFeatureClasses()
cursor = arcpy.da.SearchCursor(inputFrame,["TID","SHAPE@"])
for row in cursor:
    arcpy.CreateFileGDB_management(outputDir,row[0],"")
    for inputFC in inputFCs:
        outputFC = outputDir + os.sep + row[0] +".gdb" + os.sep + inputFC
        arcpy.Clip_analysis(inputGDB+ os.sep + inputFC, row[1], outputFC)
if __name__=="__main__":
    splitGDB(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])