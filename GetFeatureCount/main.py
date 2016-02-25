#coding=utf-8
# -*- coding: UTF-8 -*-    

# Date: 2015/10/13

import os
import sys
import time
import arcpy
from arcpy import env

import getfeaturecount
#useage:
#delete fiels in gdb with setting files.
#
indir = r"D:\ZHX\ZHXIN"
outdir = r"D:\ZHX\ZHXOUT"
outfile = r"o.txt"

print time.strftime("start:%Y/%m/%d:%H:%M:%S")
getfeaturecount.Do(indir,outdir,outfile)
print time.strftime("done:%Y/%m/%d:%H:%M:%S")
test=raw_input("press any key to quit")
