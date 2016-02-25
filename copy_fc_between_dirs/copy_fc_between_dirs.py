#coding=utf-8
# -*- coding: UTF-8 -*-

# Description: Copy specified feature class between GDB Directions 
#   功能描述：在文件地理数据库路径间复制指定的要素类

# Date: 2015/10/13

# Author:Zhang Huaixiang

import os
import arcpy

def Do(dir_src,dir_tar,ds,fc):
	pass
    # Get the list of GDBs
    # 获得文件地理数据列表
    env.workspace = dir_src

    gdblist = arcpy.ListWorkspaces("*","FileGDB")

    for gdb in gdblist:
        fc_src = dir_src + os.sep + gdb + os.sep + ds + os.sep + fc
        fc_tar = dir_tar + os.sep + gdb + os.sep + ds + os.sep + fc
        print 'Copying ' + gdb + os.sep + fc+ ' from ' + dir_src + ' to ' + dir_tar
        arcpy.Copy_management(fc_src,fc_tar)
    print 'done'
if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    Do(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")