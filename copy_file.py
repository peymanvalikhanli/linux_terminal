#!/usr/bin/python

import sys
from shutil import copyfile
import os 
from os import listdir
from os.path import isfile, join


dir_from = sys.argv[1]
dir_to = sys.argv[2]

onlyfiles = [f for f in listdir(dir_from) if isfile(join(dir_from, f))]

for f in onlyfiles:
    if not isfile(dir_to+f): 
        # print('no copy ... ')
        # print(f)
    # else: 
        copyfile(dir_from+f, dir_to+f)
        # print(f)
