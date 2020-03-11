#!/usr/bin/python

import sys
from shutil import copyfile
import os 
from os import listdir
from os.path import isfile, join

dir_from = sys.argv[1]
dir_to = sys.argv[2]

onlyfiles = [f for f in listdir(dir_from) if isfile(join(dir_from, f))]
# print onlyfiles

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
for f in onlyfiles:
    copyfile(dir_from+f, dir_to+f)
