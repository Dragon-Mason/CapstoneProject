#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:00:12 2021

@author: longzhang
"""


# we will use the datasets in this website. RAP	252 (20km) - Domain
# From 08/01/2020 to 01/31/2021
# https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/rapid-refresh-rap

import pygrib

grbs = pygrib.open('rap_252_20210113_0000_000.grb2') # 20km resolution & pressure level
grbs = pygrib.open('rap_130_20201002_0000_000.grb2') # 13km resolution & native level
grbs = pygrib.open('rap.t00z.awp130pgrbf00.grib2') # 13 resolution & pressure level
grbs = pygrib.open('rap.t00z.awp236pgrbf00.grib2') # 40 resolution & pressure level

# Print the Inventory of grbs
for grb in grbs:
    print(grb)

# select all messages about 'temperature' in the inventory of the file
grbs.select(name='Temperature')  
len(grbs.select(name='Temperature'))
# select all messages about 'relative humidity' in the inventory of the file
grbs.select(name='Relative humidity')
len(grbs.select(name='Relative humidity'))
# select all messages about 'geopotential height' in the inventory of the file
grbs.select(name='Geopotential Height')
len(grbs.select(name='Geopotential Height'))
 
# pressure levels: from 10000 Pa to 100000 Pa in units of 2500 Pa: 37 levels
############ pressure level 10000 Pascal (100 mb): ######################

# Temperature [K]
TMP_grb10000 = grbs.select(name='Temperature')[0] # The first message of 'temperature'. Pressure level = 10000 Pa
TMP_grb10000_values = TMP_grb10000.values # retrieve all data in the horizontal grid
TMP_grb10000_values.shape, TMP_grb10000_values.min(), TMP_grb10000_values.max()
TMP_lats10000, TMP_lons10000 = TMP_grb10000.latlons() # retrieve the latitude and longitude
TMP_lats10000.shape, TMP_lats10000.min(), TMP_lats10000.max(), TMP_lons10000.shape, TMP_lons10000.min(), TMP_lons10000.max()

# Relative humidity [%]
RH_grb10000 = grbs.select(name='Relative humidity')[0]
RH_grb10000_values = RH_grb10000.values
RH_grb10000_values.shape, RH_grb10000_values.min(), RH_grb10000_values.max()
RH_lats10000, RH_lons10000 = RH_grb10000.latlons()
RH_lats10000.shape, RH_lats10000.min(), RH_lats10000.max(), RH_lons10000.shape, RH_lons10000.min(), RH_lons10000.max()

# Geopotential Height [gpm]
HGT_grb10000 = grbs.select(name='Geopotential Height')[0]
HGT_grb10000_values = HGT_grb10000.values
HGT_grb10000_values.shape, HGT_grb10000_values.min(), HGT_grb10000_values.max()
HGT_lats10000, HGT_lons10000 = HGT_grb10000.latlons()
HGT_lats10000.shape, HGT_lats10000.min(), HGT_lats10000.max(), HGT_lons10000.shape, HGT_lons10000.min(), HGT_lons10000.max()


############ pressure level 12500 Pascal (125 mb): ######################

# Temperature [K]
TMP_grb12500 = grbs.select(name='Temperature')[1]
TMP_grb12500_values = TMP_grb12500.values
TMP_grb12500_values.shape, TMP_grb12500_values.min(), TMP_grb12500_values.max()
TMP_lats12500, TMP_lons12500 = TMP_grb12500.latlons()
TMP_lats12500.shape, TMP_lats12500.min(), TMP_lats12500.max(), TMP_lons12500.shape, TMP_lons12500.min(), TMP_lons12500.max()

# Relative humidity [%]
RH_grb12500 = grbs.select(name='Relative humidity')[1]
RH_grb12500_values = RH_grb12500.values
RH_grb12500_values.shape, RH_grb12500_values.min(), RH_grb12500_values.max()
RH_lats12500, RH_lons12500 = RH_grb12500.latlons()
RH_lats12500.shape, RH_lats12500.min(), RH_lats12500.max(), RH_lons12500.shape, RH_lons12500.min(), RH_lons12500.max()

# Geopotential Height [gpm]
HGT_grb12500 = grbs.select(name='Geopotential Height')[1]
HGT_grb12500_values = HGT_grb12500.values
HGT_grb12500_values.shape, HGT_grb12500_values.min(), HGT_grb12500_values.max()
HGT_lats12500, HGT_lons12500 = HGT_grb12500.latlons()
HGT_lats12500.shape, HGT_lats12500.min(), HGT_lats12500.max(), HGT_lons12500.shape, HGT_lons12500.min(), HGT_lons12500.max()




TMP_lats10000 - TMP_lats12500
TMP_lats10000 - RH_lats10000


grbs.close() # close the grib file.
