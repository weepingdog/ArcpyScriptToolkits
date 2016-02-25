#coding=utf-8
# -*- coding: UTF-8 -*-

# Description: Delete specified feature class in GDBs 
#   功能描述：删除多个文件地理数据库内指定的要素类

# Date: 2015/10/13

# Author:Zhang Huaixiang

import os
import arcpy


def Do():
    # Get the list of GDBs
    # 获得文件地理数据列表
    GDBs=os.listdir(indir)
    
    for thegdb in GDBs:
        fc_del = indir + os.sep + thegdb + os.sep + ds + os.sep + fc 
        print 'deleting ' + fc_del
        arcpy.Delete_management(fc_del) 
    print 'done'
if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    Do(sys.argv[1],sys.argv[2]],sys.argv[3])
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")