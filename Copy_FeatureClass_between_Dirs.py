
#coding=utf-8
# -*- coding: UTF-8 -*-

# Description: Copy specified feature class between GDB Directions 
#   功能描述：在文件地理数据库路径间复制指定的要素类

# Date: 2015/10/13

# Author:Zhang Huaixiang

import os
import arcpy

# Set source direction
# 设置文件地理数据库所在的源路径
dir_src = 'D:\py\inpath'

# Set target direction
# 设置文件地理数据库所在的目标路径
dir_tar = 'D:\py\outpath'

# Set Data Set
# 设置数据集名称
ds = 'AD'

# Set Feature Class
# 设置要素类名称
fc = 'LCA'

# Get the list of GDBs
# 获得文件地理数据列表
GDBs=os.listdir(dir_src)

for thegdb in GDBs:
    fc_src = dir_src + os.sep + thegdb + os.sep + ds + os.sep + fc
    fc_tar = dir_tar + os.sep + thegdb + os.sep + ds + os.sep + fc
    print 'Copying ' + thegdb + os.sep + fc+ ' from ' + dir_src + ' to ' + dir_tar
    arcpy.Copy_management(fc_src,fc_tar)
print 'done'
