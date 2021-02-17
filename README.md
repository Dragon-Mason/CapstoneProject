# CapstoneProject
Machine Learning Forecasting of Ice Super Saturated Regio ns (ISSR) in the Atmosphere

# Dataset
## Overview
Website of [RAP](https://rapidrefresh.noaa.gov/)

Originally, we want to use the data with **40-km resolution** (Horizontal grid: 225*301 cells) and **pressure levels** (the third row) in [this website](https://www.nco.ncep.noaa.gov/pmb/products/rap/). However, the provided [NCEP FTP SERVER](ftp://ftp.ncep.noaa.gov/pub/data/nccf/com/rap/prod) stores the real-time data. It only includes the data of past 2 days. And there is only [the archive of hybrid (native) grids](http://soostrc.comet.ucar.edu/data/grib/rap/), which don’t have variable “relative humidity”.  

So, we will use the datasets in [this website](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/rapid-refresh-rap). 
- Grid/Scale: RAP	252 (20km) - Domain
- Time range: From 11/01/2020 to 01/30/2021
- The data at 19:00 on 2020/12/11 is missing. So, we use the 1-hour forecasting data at 18:00 to estimate the data at 19:00.
- [Inventory of files](https://www.nco.ncep.noaa.gov/pmb/products/rap/rap.t00z.awp252pgrbf00.grib2.shtml)
- Horizontal grid: 225*301 cells
- Vertical pressure levels: from 10000 Pa to 100000 Pa in units of 2500 Pa: 37 levels

To reduce the number of data cells for analysis without losing fidelity (i.e. accuracy), we will combine adjacent 20kmx20km cells to make 40kmx40km. 

[This file](explore_data.py) is the code of data exploration.

## Download datasets

1. Use `urlretrieve` from `urllib.request` to download files
2. Use `pygrib` to parse the data


[This](collect_links_names.py) is the code to export [links](linkFile.txt) and [names](nameFile.txt) of all grib2 files from 11/01/2020 to 01/30/2021.

**To download all grib2 files from 11/01/2020 to 01/30/2021**, please
- Download the two files first: [linkFile.txt](linkFile.txt) and [nameFile.txt](nameFile.txt)
- Download and run the .py file: [download_data.py](download_data.py)

There are (31+30+31+30+31+30)*24=4392 files. The size of each one is around 9 MB. The size of all files is estimated as **40 GB**.






