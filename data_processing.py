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
            "altitude_height": V5,
            "lat_id": V6, 
            "lon_id": V7, 
            "latitude": V8, 
            "longitude": V9, 
            "geopotential_height": V10, 
            "temperature": V11, 
            "relative_humidity": V12, 
            "ISSR": V13
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

# change the directory first
os.chdir('/Volumes/Long_long/DAEN690')
# the directory of the output files
directory = '/Volumes/Long_long/DAEN690_OutputData'

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
  
ISSR_summary = [] # To store the number of ISSR cells in each file (at each date time)

# for i in range(len(grib_names)): # To run all files
# for i in range(24): # To run the 24 hours on the first day
for i in midnight_noon:
    # datetime_id = i+1 
    date_id = i//24 + 1 # V1 
    grib_name = grib_names[i]
    split_name = grib_name.split('_')
    date = split_name[2]  # V2
    hour = int(int(split_name[3])/100) # V3
 
    grbs = pygrib.open(grib_name) # open grib2 file
    V1 = []; V2 = []; V3 = []; V4 = []; V5 = []; V6 = []
    V7 = []; V8 = []; V9 = []; V10 = []; V11 = []; V12 = []; V13 = []
    
    
    count_ISSR = 0 # number of ISSR cells
    
    # from level 10000 to level 100000 in units of 2500: 37 levels
    for j in range(37):
        pressure_level = 10000+j*2500 # V4
        altitude_height = pressure_level # V5
        
        # retrieve 'Temperature', 'Relative humidity', 'Geopotential Height', lats, and lons 
        TMP = grbs.select(name='Temperature')[j]
        TMP_values = TMP.values
        RH = grbs.select(name='Relative humidity')[j]
        RH_values = RH.values
        HGT = grbs.select(name='Geopotential Height')[j+1] # the first element is not the data of level 10000
        HGT_values = HGT.values
        TMP_lats, TMP_lons = TMP.latlons()
        
        # Combine cells and store the data in a dataframe
        # drop the last(highest) altitude and the last(eastest) longitude
        for x in range(112):
            lat_id = x+1 # V6
            for y in range(150):
                lon_id = y+1 # V7
                latitude = (TMP_lats[2*x][2*y] + TMP_lats[2*x+1][2*y] + TMP_lats[2*x][2*y+1] + TMP_lats[2*x+1][2*y+1])/4 # V8
                longitude = (TMP_lons[2*x][2*y] + TMP_lons[2*x+1][2*y] + TMP_lons[2*x][2*y+1] + TMP_lons[2*x+1][2*y+1])/4 # V9
                geopotential_height = (HGT_values[2*x][2*y] + HGT_values[2*x+1][2*y] + HGT_values[2*x][2*y+1] + HGT_values[2*x+1][2*y+1])/4 # V10
                temperature = min([TMP_values[2*x][2*y], TMP_values[2*x+1][2*y], TMP_values[2*x][2*y+1], TMP_values[2*x+1][2*y+1]])  # V11
                relative_humidity = max([RH_values[2*x][2*y], RH_values[2*x+1][2*y], RH_values[2*x][2*y+1], RH_values[2*x+1][2*y+1]]) # V12
                if (temperature <= 233) & (relative_humidity >= 90):
                    # https://esd.copernicus.org/articles/6/555/2015/
                    ISSR = 'Y' # V13
                    count_ISSR = count_ISSR +1
                    
                else:
                    ISSR = 'N' # V13
                
                V1.extend([date_id])
                V2.extend([date])
                V3.extend([hour])
                V4.extend([pressure_level])
                V5.extend([altitude_height])
                V6.extend([lat_id])
                V7.extend([lon_id])
                V8.extend([latitude])
                V9.extend([longitude])
                V10.extend([geopotential_height])
                V11.extend([temperature])
                V12.extend([relative_humidity])
                V13.extend([ISSR])                
    record = {
            "date_id": V1, 
            "date": V2, 
            "hour": V3, 
            "pressure_level": V4, 
            "altitude_height": V5,
            "lat_id": V6, 
            "lon_id": V7, 
            "latitude": V8, 
            "longitude": V9, 
            "geopotential_height": V10, 
            "temperature": V11, 
            "relative_humidity": V12, 
            "ISSR": V13
            }
    df = pd.DataFrame.from_dict(record)
    df.to_csv (directory+'/'+ grib_name + '.csv', index = False, header=True)
    
    ISSR_summary.extend([count_ISSR])
    grbs.close()
    
    print(grib_name)



# Output a csv file to summary the number of ISSR cells in each grib2 file.
ISSR_summary_dic = {
                    "file names": grib_names,
                    "count of ISSRs": ISSR_summary}
ISSR_summary_df = pd.DataFrame.from_dict(ISSR_summary_dic)
ISSR_summary_df.to_csv (directory+'/'+ 'ISSR_Summary.csv', index = False, header=True)



