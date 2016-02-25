import os
import arcpy
from arcpy import env
import time

def SplitGDB(inputGDB,inputFrame,splitField,outputDir):
    # Create GDBs
    cursor = arcpy.da.SearchCursor(inputFrame,["TID"])
    for row in cursor:
        arcpy.CreateFileGDB_management(outputDir,row[0],"")
        
    # Get FCs to be cliped
    env.workspace = inputGDB
    inputFCs = arcpy.ListFeatureClasses()
    countFCs =len(inputFCs)

    # Split GDBs by feature classes
    index = 1
    for inputFC in inputFCs:
        print time.strftime("%H:%M:%S "),index,r"/", countFCs, inputFC
        cursor = arcpy.da.SearchCursor(inputFrame,["TID","SHAPE@"])
        for row in cursor:
            outputFC = outputDir + os.sep + row[0] +".gdb" + os.sep + inputFC
            arcpy.Clip_analysis(inputGDB+ os.sep + inputFC, row[1], outputFC)
        index += 1
if __name__=="__main__":
    splitGDB(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

        

