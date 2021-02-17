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


with open("nameFile.txt", "r") as file1:
    grib_names = file1.read()
    grib_names = grib_names.split("\n")
with open("linkFile.txt", "r") as file2:
    grib_links = file2.read()
    grib_links = grib_links.split("\n")

 
# download all files
for i in range(len(grib_names)):
    urlretrieve(grib_links[i], grib_names[i])

