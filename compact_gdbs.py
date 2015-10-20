#coding = utf-8
# -*- coding: UTF-8 -*-

import os
import arcpy
from arcpy import env

#输入参数
#---GDBs所在的路径
gdb_dir_in = u'E:/ZHX/ZHXIN'

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
