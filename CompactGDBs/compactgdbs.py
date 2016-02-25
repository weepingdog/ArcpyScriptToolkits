#coding = utf-8
# -*- coding: UTF-8 -*-

import os
import arcpy
from arcpy import env

#输入参数
#---GDBs所在的路径
def Do(gdb_dir_in):
    env.workspace = gdb_dir_in
    GDBs = arcpy.ListWorkspaces()
    GDBcount = len(GDBs)
    print str(GDBcount) + ' gdbs to be compacted'
    gdb_index = 1
    for gdb in GDBs:
        if gdb[-4:] in [".gdb"]:
            arcpy.Compact_management(gdb)
            print str(gdb_index) + '\t' + gdb + ' done'
        else:
            print str(gdb_index) + '\t' + gdb + ' is not a gdb file'
        gdb_index = gdb_index + 1
if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    Do(sys.argv[1])
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")