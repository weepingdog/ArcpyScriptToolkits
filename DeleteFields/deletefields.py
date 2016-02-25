#coding=utf-8
# -*- coding: UTF-8 -*-   

#Author: zhang huaixiang
#Email: farewellwhu@gmail.com
#Date:20160225

import os
import sys
import time

import arcpy
from arcpy import env

#useage:
#delete fiels in gdb with setting files.
#
def DeleteFiels(gdppath,dictDeleteFeatureClassFields):    
    dictFeatureClassesInGDB = {}
    env.workspace = gdppath
    listFeatureClass = arcpy.ListFeatureClasses()
    for featureClass in listFeatureClass:
        dictFeatureClassesInGDB[featureClass] = env.workspace
    listDataSets = arcpy.ListDatasets()
    for dataSet in listDataSets:
        env.workspace = os.path.join(gdppath,dataSet)
        listFeatureClassesInDataSets = arcpy.ListFeatureClasses()
        for featureClass in listFeatureClassesInDataSets:
            dictFeatureClassesInGDB[featureClass] = env.workspace
    for (featureClass, featureClassPath) in dictFeatureClassesInGDB.items():
        if(dictDeleteFeatureClassFields.has_key(featureClass)):
            env.workspace = featureClassPath
            arcpy.DeleteField_management(featureClass,dictDeleteFeatureClassFields[featureClass])
            print "delete field:{0} in featureClass:{1} of space:{2}".format(dictDeleteFeatureClassFields[featureClass],featureClass,featureClassPath)

def  GetDictFeatureClassFiels(settingpath):
    dictFeatureClassFields = {}
    with open(settingpath,"r") as f:
        readline = f.readline()
        while(readline):
            readline.strip("\n")
            featureClass,field = readline.split(",")
            if(field[-1]=="\n"):
                field=field[:-1]
            if(featureClass and field):
                if(dictFeatureClassFields.has_key(featureClass)):
                    dictFeatureClassFields[featureClass] += field
                else:
                    dictFeatureClassFields[featureClass] = []
                    dictFeatureClassFields[featureClass] += field
                readline = f.readline()
            else:
                readline = f.readline()
                continue
    return dictFeatureClassFields
def Do(gdppath, settingpath):
    dictDeleteFeatureClassFields = GetDictFeatureClassFiels(settingpath)
    DeleteFiels(gdppath, dictDeleteFeatureClassFields)
    
if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    Do(sys.argv[1],sys.argv[2])
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")
