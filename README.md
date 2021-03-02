# CapstoneProject
Machine Learning Forecasting of Ice Super Saturated Regions (ISSR) in the Atmosphere

# 1. Dataset
## 1.1. Overview
Website of [RAP](https://rapidrefresh.noaa.gov/)

Originally, we want to use the data with **40-km resolution** (Horizontal grid: 225*301 cells) and **pressure levels** (the third row) in [this website](https://www.nco.ncep.noaa.gov/pmb/products/rap/). However, the provided [NCEP FTP SERVER](ftp://ftp.ncep.noaa.gov/pub/data/nccf/com/rap/prod) stores the real-time data. It only includes the data of past 2 days. And there is only [the archive of hybrid (native) grids](http://soostrc.comet.ucar.edu/data/grib/rap/), which don’t have variable “relative humidity”.  

So, we will use the datasets in [this website](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/rapid-refresh-rap). 
- Grid/Scale: RAP	252 (20km) - Domain
- Time range: From 17/05/2020 to 12/31/2020
- The data at 19:00 on 2020/12/11 is missing. So, we use the 1-hour forecasting data at 18:00 to estimate the data at 19:00.
- [Inventory of files](https://www.nco.ncep.noaa.gov/pmb/products/rap/rap.t00z.awp252pgrbf00.grib2.shtml)
- Horizontal grid: 225*301 cells
- Vertical pressure levels: from 10000 Pa to 100000 Pa in units of 2500 Pa: 37 levels

To reduce the number of data cells for analysis without losing fidelity (i.e. accuracy), we will combine adjacent 20kmx20km cells to make 40kmx40km. 

[This file](explore_data.py) is the code of data exploration (grib2).

## 1.2. Download datasets

1. Use `urlretrieve` from `urllib.request` to download files
2. Use `pygrib` to parse the data
3. [This](collect_links_names.py) is the code to export [links](linkFile.txt) and [names](nameFile.txt) of all grib2 files from 17/05/2020 to 12/31/2020.
4. **To download all grib2 files from 17/05/2020 to 12/31/2020**, please
    - Download the two files first: [linkFile.txt](linkFile.txt) and [nameFile.txt](nameFile.txt)
    - Download and run the .py file: [download_data.py](download_data.py)
    - There are 5496 files. The size of each one is around 9 MB. The size of all files is estimated as **48 GB**.

## 1.3. Data Processing


1. Retrieve and create 14 variables for each grib2 file{
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
            "ISSR": V13}
2. Combine cells, label issr
3. Output a csv file with all records for each grib2 file
4. Output a csv file with only 'Y' records for each grib2 file
5. [Code](data_processing.py)
    - Estimated time: 75s each grib2 file
    - Estimated size: 86 Mb for all records/ 200 Kb for ‘Y’ records
    - Totally: 5496 files
6. Task Assignment:
    - Only modify the range in for-loop to download data and clean data

|Task|Days(229)|ID(229*24=5496)|Date|Python for-loop Range|Assignee|
|----|---------|---------------|----|------------|--------|
|Task1|19|1 - 456|20200517 - 20200604 |range(0,456)|Wei Wang|
|Task2|19|457 - 912|20200605 - 20200623|range(456, 912)|Wei Wang|
|Task3|19|913 - 1368|20200624 - 20200712|range(912, 1368)|Baizhong|
|Task4|19|1369 - 1824|20200713 - 20200731|range(1368, 1824)|Baizhong|
|Task5|19|1825 - 2280|20200801 - 20200819|range(1824, 2280)|Wenpeng|
|Task6|19|2281 - 2736|20200820 - 20200907|range(2280, 2736)|Wenpeng|
|Task7|19|2737 - 3192|20200908 - 20200926|range(2736, 3192)|Lee|
|Task8|19|3193 - 3648|20200927 - 20201015|range(3192, 3648)|Lee|
|Task9|19|3649 - 4104|20201016 - 20201103|range(3648, 4104)|Iwan|
|Task10|19|4105 - 4560|20201104 - 20201122|range(4104, 4560)|Iwan|
|Task11|19|4561 - 5016|20201123 - 20201211|range(4560, 5016)|Long|
|Task12|20|5017 - 5496|20201212 - 20201231|range(5016, 5496)|Long|


## 1.4 Data Exploration

- Directly use the following two csv files to make data exploration. They are generated using [summary_tables.R](summary_tables.R), [nameFile.txt](nameFile.txt), and [all datasets with only 'yes' labels](https://exchangelabsgmu-my.sharepoint.com/personal/lzhang30_masonlive_gmu_edu/_layouts/15/onedrive.aspx?id=%2Fsites%2FDAEN%2D690%2DDragon%2FShared%20Documents&listurl=https%3A%2F%2Fexchangelabsgmu%2Esharepoint%2Ecom%2Fsites%2FDAEN%2D690%2DDragon%2FShared%20Documents).
    - [overall_summary.csv](overall_summary.csv) is the volume of ISSRs in 3D grid at each datetime (hourly time).
    - [layer_summary.csv](layer_summary.csv) is the volume of ISSRs in 2D/Horizontal grids (each pressure level) at each datetime (hourly time).
    - [latitude_summary.csv](latitude_summary.csv) is the count of ISSR cells in each latitude at each datetime.
    - [longitude_summary.csv](longitude_summary.csv) is the count of ISSR cells in each longitude at each datetime.
- [Explore.Rmd](Explore.Rmd) is a sample of data visualization. Download [Explore.html](Explore.html) to see the output.

## This is a dashboard link
- please click this link: [Explore.html](https://rpubs.com/mridwan/733180)



