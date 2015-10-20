#coding=utf-8
# -*- coding: UTF-8 -*-    

# Date: 2015/10/13

import os
import arcpy
from arcpy import env

indir = 'D:\py\inpath'

outfile = 'D:\py\inpath\o.txt'
f = open(outfile,'w')
GDBs=os.listdir(indir)

for thegdb in GDBs:
    ws_gdb = indir + os.sep +thegdb
    env.workspace = ws_gdb
    fcs_in_gdb = arcpy.ListFeatureClasses()
    for fc in fcs_in_gdb:
        fc_dir = env.workspace + os.sep + fc
        fc_count = arcpy.GetCount_management(fc_dir)
        print fc_dir,fc_count
        f.write(fc_dir+'\t'+str(fc_count))
    dss_in_gdb = arcpy.ListDatasets()
    for ds in dss_in_gdb:
        ws_ds = ws_gdb + os.sep +ds
        env.workspace = ws_ds
        fcs_in_ds = arcpy.ListFeatureClasses()
        for fc in fcs_in_ds:
            fc_dir = env.workspace + os.sep+ fc
            fc_count = arcpy.GetCount_management(fc_dir)
            print fc_dir, fc_count
            f.write(fc_dir+'\t'+str(fc_count))
f.close()
