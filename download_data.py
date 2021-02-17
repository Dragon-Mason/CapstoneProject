#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:29:12 2021

@author: longzhang
"""

from urllib.request import urlretrieve
import os

# change the direction first
os.chdir('/Volumes/Long_long/DAEN690')

# load links and names of grib2 files
with open("nameFile.txt", "r") as file1:
    grib_names = file1.read().split("\n")
    grib_names.pop()
with open("linkFile.txt", "r") as file2:
    grib_links = file2.read().split("\n")
    grib_links.pop()

# download all grib2 files
for i in range(len(grib_names)):
    urlretrieve(grib_links[i], grib_names[i])

