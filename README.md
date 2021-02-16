# CapstoneProject
Machine Learning Forecasting of Ice Super Saturated Regio ns (ISSR) in the Atmosphere

## Data Sets
Website of [RAP](https://rapidrefresh.noaa.gov/)

Originally, we want to use the data with **40-km resolution** (Horizontal grid: 225*301 cells) and **pressure levels** (the third row) in [this website](https://www.nco.ncep.noaa.gov/pmb/products/rap/). However, the provided [NCEP FTP SERVER](ftp://ftp.ncep.noaa.gov/pub/data/nccf/com/rap/prod) stores the real-time data. It only includes the data of past 2 days. And there is only [the archive of hybrid (native) grids](http://soostrc.comet.ucar.edu/data/grib/rap/), which don’t have variable “relative humidity”.  

So, we will use the datasets in [this website](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/rapid-refresh-rap). 
- Grid/Scale: RAP	252 (20km) - Domain
- Time range: From 08/01/2020 to 01/31/2021
- [Inventory of files](https://www.nco.ncep.noaa.gov/pmb/products/rap/rap.t00z.awp252pgrbf00.grib2.shtml)
- Horizontal grid: 225*301 cells
- Vertical pressure levels: from 10000 Pa to 100000 Pa in units of 2500 Pa: 37 levels

To reduce the number of data cells for analysis without losing fidelity (i.e. accuracy), we will combine adjacent 20kmx20km cells to make 40kmx40km. 

[This file](explore_data.py) is the code of data exploration.



