#coding=utf-8
# -*- coding: UTF-8 -*-    

# Date: 2015/10/13

import os
import arcpy
from arcpy import env


def Do(indir, outdir,outfile):
    f = open(outdir + os.sep +outfile, "w")
    
    env.workspace = indir
    gdblist = arcpy.ListWorkspaces("*", "FileGDB")
    
    for gdb in gdblist:
        print gdb
        f.write(gdb + "\r\n")
        
        gdbname = os.path.split(gdb)[1][:-4]
        f_gdb = open(outdir + os.sep + gdbname + ".txt", "w")
        
        env.workspace = gdb
        fcs_in_gdb = arcpy.ListFeatureClasses()
        for fc in fcs_in_gdb:
            fc_count = arcpy.GetCount_management(env.workspace + os.sep + fc)
            print fc, "\t", fc_count
            f.write(fc + "\t" + str(fc_count) + "\r\n")
            f_gdb.write(fc + "\t" + str(fc_count) + "\r\n")
        dss_in_gdb = arcpy.ListDatasets()
        for ds in dss_in_gdb:
            env.workspace = gdb + os.sep + ds
            fcs_in_ds = arcpy.ListFeatureClasses()
            for fc in fcs_in_ds:
                fc_count = arcpy.GetCount_management(env.workspace + os.sep + fc)
                print ds, fc, fc_count
                f.write(ds + "\t" + fc + "\t" + str(fc_count) +"\r\n")
                f_gdb.write(ds + "\t" + fc + "\t" + str(fc_count) +"\r\n")
        print "==================="
        f.write("===================\r\n")
        f_gdb.close()
    f.close()

if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    Do(sys.argv[1],sys.argv[2],sys.argv[3])
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")
