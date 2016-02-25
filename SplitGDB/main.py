import os
import arcpy
from arcpy import env
import time
import splitGDBTool

inputGDB = r"C:\Users\zhx\Desktop\321112DNT.gdb"
inputFrame = r"C:\Users\zhx\Desktop\T.gdb\F50000"
splitField = r"TID"
outputDir = r"D:\OUTPUT"

splitGDBTool.splitGDBTool(inputGDB,inputFrame,splitField,outputDir)