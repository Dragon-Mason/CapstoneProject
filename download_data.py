#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:29:12 2021

@author: longzhang
"""

import json
from urllib.request import urlretrieve

with open('grib_names.txt', 'r') as f:
    grib_names = json.loads(f.read())
with open('grib_urls.txt', 'r') as f:
    grib_urls = json.loads(f.read())
    
# download all files
for i in range(len(grib_urls)):
    urlretrieve(grib_urls[i], grib_names[i])
