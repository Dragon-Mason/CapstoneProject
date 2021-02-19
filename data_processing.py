#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:52:59 2021

@author: longzhang

1. Retrieve and create 12 variables for each grib2 file
            "date_id": V1, 
            "date": V2, 
            "hour": V3, 
            "pressure_level": V4, 
            "lat_id": V5, 
            "lon_id": V6, 
            "latitude": V7, 
            "longitude": V8, 
            "geopotential_height": V9, 
            "temperature": V10, 
            "relative_humidity": V11, 
            "ISSR": V12
2. Combine cells, label issr

3. Output a csv file for each grib2 file:

Estimated time: 68s each grib2 file
Estimated size: 73.1 Mb each csv file
Totally: 4392 files

To save time, only clean the data at midnight and noon
Midnight and noon: 366 files, 7 hour

"""

import pygrib
import pandas as pd
import os

# change the direction first
os.chdir('/Volumes/Long_long/DAEN690')
# the direction of the output files
direction = '/Volumes/Long_long/DAEN690_OutputData'

# load names of grib2 files
with open("nameFile.txt", "r") as file1:
    grib_names = file1.read().split("\n")
    grib_names.pop()

grib_names[0].split('_')
# ['rap', '252', '20200801', '0000', '000.grb2']


# To save time, only clean the data at midnight and noon
# here, generate the index of files at midnight and noon
midnight_noon = []
for i in range(len(grib_names)):
    if i%12 == 0:
        midnight_noon.extend([i])
    

# for i in range(len(grib_names)):
for i in midnight_noon:
    # datetime_id = i+1 
    date_id = i//24 + 1 # V1
    grib_name = grib_names[i]
    split_name = grib_name.split('_')
    date = split_name[2]  # V2
    hour = int(int(split_name[3])/100) # V3
 
    grbs = pygrib.open(grib_name) # open grib2 file
    V1 = []; V2 = []; V3 = []; V4 = []; V5 = []; V6 = []
    V7 = []; V8 = []; V9 = []; V10 = []; V11 = []; V12 = []
    
    # from level 10000 to level 100000 in units of 2500: 37 levels
    for j in range(37):
        pressure_level = 10000+j*2500 # V4
        
        # retrieve 'Temperature', 'Relative humidity', 'Geopotential Height', lats, and lons 
        TMP = grbs.select(name='Temperature')[j]
        TMP_values = TMP.values
        RH = grbs.select(name='Relative humidity')[j]
        RH_values = RH.values
        HGT = grbs.select(name='Geopotential Height')[j+1] # the first element is not the data of level 10000
        HGT_values = HGT.values
        TMP_lats, TMP_lons = TMP.latlons()
        
        # Combine cells and store the data in lists
        # drop the last(highest) altitude and the last(eastest) longitude
        for x in range(112):
            lat_id = x+1 # V5
            for y in range(150):
                lon_id = y+1 # V6
                latitude = (TMP_lats[2*x][2*y] + TMP_lats[2*x+1][2*y] + TMP_lats[2*x][2*y+1] + TMP_lats[2*x+1][2*y+1])/4 # V7
                longitude = (TMP_lons[2*x][2*y] + TMP_lons[2*x+1][2*y] + TMP_lons[2*x][2*y+1] + TMP_lons[2*x+1][2*y+1])/4 # V8
                geopotential_height = (HGT_values[2*x][2*y] + HGT_values[2*x+1][2*y] + HGT_values[2*x][2*y+1] + HGT_values[2*x+1][2*y+1])/4 # V9
                temperature = (TMP_values[2*x][2*y] + TMP_values[2*x+1][2*y] + TMP_values[2*x][2*y+1] + TMP_values[2*x+1][2*y+1])/4  # V10
                relative_humidity = (RH_values[2*x][2*y] + RH_values[2*x+1][2*y] + RH_values[2*x][2*y+1] + RH_values[2*x+1][2*y+1])/4 # V11
                if (temperature <= 233) & (relative_humidity >= 95):
                    # https://esd.copernicus.org/articles/6/555/2015/
                    ISSR = 'Y' # V12
                else:
                    ISSR = 'N' # V12
                
                V1.extend([date_id])
                V2.extend([date])
                V3.extend([hour])
                V4.extend([pressure_level])
                V5.extend([lat_id])
                V6.extend([lon_id])
                V7.extend([latitude])
                V8.extend([longitude])
                V9.extend([geopotential_height])
                V10.extend([temperature])
                V11.extend([relative_humidity])
                V12.extend([ISSR])                
    record = {
            "date_id": V1, 
            "date": V2, 
            "hour": V3, 
            "pressure_level": V4, 
            "lat_id": V5, 
            "lon_id": V6, 
            "latitude": V7, 
            "longitude": V8, 
            "geopotential_height": V9, 
            "temperature": V10, 
            "relative_humidity": V11, 
            "ISSR": V12
            }
    df = pd.DataFrame.from_dict(record)
    df.to_csv (direction+'/'+ grib_name + '.csv', index = False, header=True)
    grbs.close()





