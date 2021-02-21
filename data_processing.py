#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:52:59 2021

@author: longzhang

1. Retrieve and create 12 variables for each grib2 file
            "datetime_id": V0,
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
            "relative_humidity_water": V11, 
            "relative_humidity_ice": V12,
            "ISSR": V13
2. Combine cells, label issr

3. Output a csv file for each grib2 file:

Estimated time: 75s each grib2 file
Estimated size: 86 Mb for all records/ 200 Kb for ‘Y’ records
Totally: 5496 files

"""

import pygrib
import pandas as pd
import math
import os

# change the directory first
os.chdir('/Volumes/Long_long/DAEN690Dragon/GRIB2')
# the directory of the output files
directory_y_n = '/Volumes/Long_long/DAEN690Dragon/YES_NO_CSV'
directory_y = '/Volumes/Long_long/DAEN690Dragon/YES_CSV'

# load names of grib2 files
with open("nameFile.txt", "r") as file1:
    grib_names = file1.read().split("\n")
    grib_names.pop()

grib_names[0].split('_')
# ['rap', '252', '20200801', '0000', '000.grb2']

# here, generate the index of files at midnight and noon
# midnight_noon = []
# for i in range(len(grib_names)):
#     if i%12 == 0:
#         midnight_noon.extend([i])
  

# for i in range(len(grib_names)): # To run all files
# for i in midnight_noon:
for i in range(0, 456):
    datetime_id = i+1 # V0
    date_id = i//24 + 1 # V1 
    grib_name = grib_names[i]
    split_name = grib_name.split('_')
    date = split_name[2]  # V2
    hour = int(int(split_name[3])/100) # V3
 
    grbs = pygrib.open(grib_name) # open grib2 file
    V0 = []; V1 = []; V2 = []; V3 = []; V4 = []; V5 = []; V6 = []; V7 = []
    V8 = []; V9 = []; V10 = []; V11 = []; V12 = []; V13 = []
    
    
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
        
        # Combine cells and store the data in a dataframe
        # drop the last(highest) altitude and the last(eastest) longitude
        for x in range(112):
            lat_id = x+1 # V5
            for y in range(150):
                lon_id = y+1 # V6
                
                # Latitude, Longitude, and Geopotential Height of the 4 adjacent cells
                latitude = (TMP_lats[2*x][2*y] + TMP_lats[2*x+1][2*y] + TMP_lats[2*x][2*y+1] + TMP_lats[2*x+1][2*y+1])/4 # V7
                longitude = (TMP_lons[2*x][2*y] + TMP_lons[2*x+1][2*y] + TMP_lons[2*x][2*y+1] + TMP_lons[2*x+1][2*y+1])/4 # V8
                geopotential_height = (HGT_values[2*x][2*y] + HGT_values[2*x+1][2*y] + HGT_values[2*x][2*y+1] + HGT_values[2*x+1][2*y+1])/4 # V9
                
                # Temperature for each cell
                TMP1 = TMP_values[2*x][2*y]
                TMP2 = TMP_values[2*x+1][2*y]
                TMP3 = TMP_values[2*x][2*y+1]
                TMP4 = TMP_values[2*x+1][2*y+1]
                
                # Relative humidity over water for each cell
                RH_W1 = RH_values[2*x][2*y]
                RH_W2 = RH_values[2*x+1][2*y]
                RH_W3 = RH_values[2*x][2*y+1]
                RH_W4 = RH_values[2*x+1][2*y+1]
                
                # Relative humidity over ice for each cell
                RH_I1 = RH_W1*math.exp(17.2693882*(TMP1-273.16)/(TMP1-35.86))/math.exp(21.8745584*(TMP1-273.16)/(TMP1-7.66))
                RH_I2 = RH_W2*math.exp(17.2693882*(TMP2-273.16)/(TMP2-35.86))/math.exp(21.8745584*(TMP2-273.16)/(TMP2-7.66))
                RH_I3 = RH_W3*math.exp(17.2693882*(TMP3-273.16)/(TMP3-35.86))/math.exp(21.8745584*(TMP3-273.16)/(TMP3-7.66))
                RH_I4 = RH_W4*math.exp(17.2693882*(TMP4-273.16)/(TMP4-35.86))/math.exp(21.8745584*(TMP4-273.16)/(TMP4-7.66))
                
                # Temperature, RH over water, and RH over ice of the 4 adjacent cells
                temperature = sum([TMP1, TMP2, TMP3, TMP4])/4 # V10
                relative_humidity_water = sum([RH_W1, RH_W2, RH_W3, RH_W4])/4 # V11
                relative_humidity_ice = sum([RH_I1, RH_I2, RH_I3, RH_I4])/4 # V12
                
                if (temperature < 233) & (relative_humidity_ice > 100):
                    # https://esd.copernicus.org/articles/6/555/2015/
                    ISSR = 'Y' # V13                  
                else:
                    ISSR = 'N' # V13
                
                V0.extend([datetime_id])
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
                V11.extend([relative_humidity_water])
                V12.extend([relative_humidity_ice])
                V13.extend([ISSR])                
    record = {
            "datetime_id": V0,
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
            "relative_humidity_water": V11, 
            "relative_humidity_ice": V12,
            "ISSR": V13
            }
    
    # Output all records
    df = pd.DataFrame.from_dict(record)
    df.to_csv (directory_y_n+'/'+ grib_name + '.csv', index = False, header=True)
    
    # Output records with label "Y"
    df_yes = df[df['ISSR'] == 'Y']
    df_yes.to_csv (directory_y+'/'+ 'yes_' + grib_name + '.csv', index = False, header=True)
    
    grbs.close()
    
    print(grib_name + " >>> Done!")





