#coding=utf-8
# -*- coding: UTF-8 -*-

# Description: Delete specified feature class in GDBs 
#   功能描述：删除多个文件地理数据库内指定的要素类

# Date: 2015/10/13

# Author:Zhang Huaixiang

import os
import arcpy

# Set input direction
# 设置文件地理数据库所在的路径
indir = 'D:\py\inpath'

# Set Data Set
# 设置数据集名称
ds = 'AD'

# Set Feature Class
# 设置要素类名称
fc = 'LCA'


# Get the list of GDBs
# 获得文件地理数据列表
GDBs=os.listdir(indir)

for thegdb in GDBs:
    fc_del = indir + os.sep + thegdb + os.sep + ds + os.sep + fc 
    print 'deleting ' + fc_del
    arcpy.Delete_management(fc_del) 
print 'done'
