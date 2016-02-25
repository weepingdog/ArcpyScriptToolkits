#coding=utf-8
# -*- coding: UTF-8 -*-   

#Author: zhang huaixiang
#Email: farewellwhu@gmail.com
#Date:20160225

import os
import sys
import time

import arcpy
from arcpy import env

import deletefields

#useage:
#delete fiels in gdb with setting files.
#
gdppath = r"D:\ZHX\ZHXIN\A1.gdb"
settingpath = r"C:\Users\zhx\Desktop\doc2016\gdbs\Book1.csv"
print time.strftime("start:%Y/%m/%d:%H:%M:%S")
deletefields.Do(gdppath,settingpath)
print time.strftime("done:%Y/%m/%d:%H:%M:%S")
test=raw_input("press any key to quit")
