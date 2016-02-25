#coding=utf-8
# -*- coding: UTF-8 -*-

# Description: Delete specified feature class in GDBs 
#   功能描述：删除多个文件地理数据库内指定的要素类

# Date: 2015/10/13

# Author:Zhang Huaixiang

import os
import sys
import time

import arcpy
from arcpy import env

import deletefcingdbs

# Set input direction
# 设置文件地理数据库所在的路径
indir = 'D:\py\inpath'

# Set Data Set
# 设置数据集名称
ds = 'AD'

# Set Feature Class
# 设置要素类名称
fc = 'LCA'
if __name__=="__main__":
    print time.strftime("start:%Y/%m/%d:%H:%M:%S")
    deletefcingdbs.Do(indir,ds,fc)
    print time.strftime("done:%Y/%m/%d:%H:%M:%S")
