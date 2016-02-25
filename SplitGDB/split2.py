import os
import arcpy
from arcpy import env
import time

def splitGDB2(inputGDB,inputFrame,splitField,outputDir):
    # Get FCs to be cliped
    env.workspace = inputGDB
    inputFCs = arcpy.ListFeatureClasses()
    countFCs =len(inputFCs)
    # 
    cursor = arcpy.da.SearchCursor(inputFrame,["TID","SHAPE@"])
    index = 1
    for row in cursor:
        arcpy.CreateFileGDB_management(outputDir,row[0],"")
        print index,time.strftime("%H:%M:%S "),row[0]+".gdb"
        indexfc = 1
        for inputFC in inputFCs:
            print "\t",index,"-",indexfc, time.strftime("%H:%M:%S "), inputFC
            outputFC = outputDir + os.sep + row[0] +".gdb" + os.sep + inputFC
            arcpy.Clip_analysis(inputGDB+ os.sep + inputFC, row[1], outputFC)
            indexfc += 1
        index += 1
if __name__=="__main__":
    splitGDB2(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])