import os
import arcpy
from arcpy import env
def Do(gdb_in,gdb_out):
    path_gdb_out=os.path.dirname(gdb_out)
    name_gdb_out=os.path.basename(gdb_out)
    if arcpy.Exists(gdb_out):
        arcpy.Delete_management(gdb_out)
    arcpy.CreateFileGDB_management(path_gdb_out,name_gdb_out)    
    env.workspace=gdb_in
    fcs=arcpy.ListFeatureClasses()
    fldsName_not_dissolve=[u"OBJECTID",u"SHAPE",u"SHAPE_Length",u"SHAPE_Area"]
    for fc in fcs:
        flds_dissolve=[]
        fc_in=gdb_in+os.sep+fc
        fc_out=gdb_out+os.sep+fc
        desc=arcpy.Describe(fc)
        if not desc.shapeType=="Point":
        #if not fc[-1:].upper()=="P":
            flds=arcpy.ListFields(fc)
            print fc_in,fc_out
            for fld in flds:
                if not fld.baseName in fldsName_not_dissolve:
                    flds_dissolve.append(fld.baseName)
            arcpy.Dissolve_management(fc_in,fc_out,flds_dissolve,"","SINGLE_PART", "")              
        else:
            arcpy.CopyFeatures_management(fc_in,fc_out)
if __name__=="__main__":
    Do(sys.argv[1],sys.argv[2])