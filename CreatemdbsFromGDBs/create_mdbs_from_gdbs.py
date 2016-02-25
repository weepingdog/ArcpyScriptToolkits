#coding = utf-8
# -*- coding: UTF-8 -*-

import os
import arcpy
from arcpy import env

#获得GDB列表
env.workspace = gdb_dir_in
GDBlist = arcpy.ListWorkspaces()

gdb_index = 1
mdblist = []
for gdb in GDBlist:
    if gdb[-4:] in [".gdb"]:
        gdbname = os.path.split(gdb)[1]
        mdbname = gdbname[:-4] + '.mdb'
        mdb = mdb_dir_out + os.sep +mdbname
        if arcpy.Exists(mdb):
            os.remove(mdb)
        arcpy.CreatePersonalGDB_management(mdb_dir_out,mdbname)
        env.workspace = gdb
        fcs_in_gdb = arcpy.ListFeatureClasses()
        arcpy.FeatureClassToGeodatabase_conversion(fcs_in_gdb,mdb)
        print str(gdb_index) + '\t' + gdb + ' translate to mdb done!'
    else:
        print str(gdb_index) + '\t' + gdb + ' is not a gdb file'
        continue
    gdb_index = gdb_index + 1
if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    Do(sys.argv[1],sys.argv[2]])
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")