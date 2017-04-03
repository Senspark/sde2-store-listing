#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "python ../../../store-listing-toolkit/populate-v3.py metadata -platform iOS -prj-path . -sheet 1XQA-l4YzgxYOJsk1ai1T0s8V__Fi4hAImzDQIUENoh8 -customized-metadata-path ../src/itunes/metadata"
print cmd
os.system(cmd)
