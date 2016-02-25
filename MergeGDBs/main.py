import os
import sys
import time

import arcpy
from arcpy import env

import mergegdbs

#1.--输入GDBs所在的路径
in_path = 'E:/ZHX/ZHXIN'

#2.1--输出gdb所在的路径
out_path = 'E:/ZHX/ZHXOUT'

#2.2--输出gdb的名字
out_gdb = 'output.gdb'

#3--图层名列表
fcs = [u'LRDL', u'BOUA5', 'LCA']

print time.strftime("start:%Y/%m/%d:%H:%M:%S")
mergegdbs.Do(in_path,out_path,out_gdb,fcs)
print time.strftime("done:%Y/%m/%d:%H:%M:%S")
test=raw_input("press any key to quit")
