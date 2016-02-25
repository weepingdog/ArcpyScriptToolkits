#coding = utf-8
# -*- coding: UTF-8 -*-

import os
import arcpy
from arcpy import env

import createmdbsfromgdbs
#输入参数
#1---GDBs所在的路径
gdb_dir_in = u'E:/ZHX/ZHXIN'

#输出参数
#2---输出MDB所在的路径
mdb_dir_out = u'E:/ZHX/ZHXOUT'

print time.strftime("start:%Y/%m/%d:%H:%M:%S")
createmdbsfromgdbs.Do(gdb_dir_in,mdb_dir_out)
print time.strftime("done:%Y/%m/%d:%H:%M:%S")

