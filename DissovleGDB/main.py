import os
import arcpy
from arcpy import env

import dissovle
gdb_in = r'C:\Users\pc\Desktop\TS1000\input.gdb'
gdb_out = r'C:\Users\pc\Desktop\TS1000\output.gdb'

dissovle.Do(gdb_in,gdb_out)