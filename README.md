# CapstoneProject: Machine Learning Forecasting for ISSR Volumetric Evolution

- DAEN-690-Spring 2021
- **Team Dragon**: Long Zhang, Dohyung Lee, Mohammad Ridwan, Wei Wang, Wenpeng Hao, Baizhong Hou
- **Mentor**: Prof. Lance Sherry
- **Instructor**: Prof. F. Brett Berlin 


Ice Super Saturated Region (ISSR) is the atmospheric condition for the formation of Contrail-Cirrus Clouds which are estimated to contribute 2% of the Earth’s total anthropogenic global warming. This project aims to predict the volumetric evolution of ISSRs in each flight level in CONUS, including forecasting for volume change rate and volume magnitude, to help to facilitate the design of the air transportation system. This in turn is likely to help prevent global warming.

Firstly, we conducted comprehensive statistical analyses and visualizations for the volumetric evolution of ISSRs in CONUS in 2020 to find out potential patterns about ISSRs, including ISSR volume by hour/day/month, ISSR ceilings and floors by hour/day/month, and ISSR volume at different flight levels/latitude/longitude. Then, multiple machine learning time-series models were applied to the prediction for short-term (the prediction cycle of 1 hour), intermediate-term (the prediction cycle of 24 hour), and long-term (the prediction cycle of 48 hour) change rate for ISSR volume. The models we used were linear regression (LR), multilayer perceptron (MLP), and long short-term memory (LSTM). Based on the predicted change rate of ISSR volume and past ISSR volume, we can calculate the prediction value for future ISSR volume. Particularly, we focused on the prediction for flight level 360 which has the highest proportion of ISSR volume. 

The results show that the three models have similar performance for short-term prediction. With the increase of prediction cycle, the performance of LR model is dramatically decreased. However, MLP and LSTM tend to be more stable, and LSTM always performs best. To sum up, it is recommended to apply LR model to short-term prediction because of its simplicity and good performance and to apply LSTM model to intermediate-term and long-term prediction. The prediction results can help policy makers understand how the ISSR percent volume in one flight level will change by time and the probability that an airplane meets ISSR in that flight level.



# 1. Dataset
## 1.1. Overview
Website of [RAP](https://rapidrefresh.noaa.gov/)

The Rapid Refresh (RAP) is the National Oceanic and Atmospheric Administration (NOAA) hourly-updated forecasting system to provide related decision-makings for applications in aviation (and transportation in general), severe weather, and energy, etc. The data in RAP system is collected from commercial aircraft weather data, balloon data, radar data, surface observations, and satellite data. It has different methods to describe map projection (like lambert conformal projection and Polar Stereographic projection), resolution grids (like 13km (337*451 cells), 20km (225*301 cells), 40km (113*151 cells)), and vertical coordinate (like isobaric levels and hybrid-pressure levels). Types of data in the system are **RAP Analysis Data** and **RAP Forecasts Data**. And the format of datasets:  **grib2**


- [Database website](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/rapid-refresh-rap)
- Type: RAP Analysis Data
- Grid/Scale: RAP	252 (20km) - Domain
- Time range: From 17/05/2020 to 12/31/2020
- The data at 19:00 on 2020/12/11 is missing. So, we use the 1-hour forecasting data at 18:00 to estimate the data at 19:00.
- [Inventory of files](https://www.nco.ncep.noaa.gov/pmb/products/rap/rap.t00z.awp252pgrbf00.grib2.shtml)
- Horizontal grid: 225*301 cells
- Vertical pressure levels: from 10000 Pa to 100000 Pa in units of 2500 Pa: 37 levels

To reduce the number of data cells for analysis without losing fidelity (i.e. accuracy), we will combine adjacent 20kmx20km cells to make 40kmx40km. 

[explore_data.py](explore_data.py) is the code of data exploration for .grib2 format file.

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

- **Dashboard**
    - Directly use the following 8 csv files to make data exploration. 
        - The following four are generated using [summary_tables.R](summary_tables.R), [nameFile.txt](nameFile.txt), and [all datasets with only 'yes' labels](https://exchangelabsgmu-my.sharepoint.com/personal/lzhang30_masonlive_gmu_edu/_layouts/15/onedrive.aspx?id=%2Fsites%2FDAEN%2D690%2DDragon%2FShared%20Documents&listurl=https%3A%2F%2Fexchangelabsgmu%2Esharepoint%2Ecom%2Fsites%2FDAEN%2D690%2DDragon%2FShared%20Documents).
            - [overall_summary.csv](overall_summary.csv) is the volume of ISSRs in 3D grid at each datetime (hourly time).
            - [layer_summary.csv](layer_summary.csv) is the volume of ISSRs in 2D/Horizontal grids (each pressure level) at each datetime (hourly time).
            - [latitude_summary.csv](latitude_summary.csv) is the count of ISSR cells in each latitude at each datetime.
            - [longitude_summary.csv](longitude_summary.csv) is the count of ISSR cells in each longitude at each datetime.
        - The following 4 files are generated by runnning code [FLs_Cells_Summary.R](FLs_Cells_Summary.R) on [nameFile.txt](nameFile.txt) and [all datasets with only 'yes' labels](https://exchangelabsgmu-my.sharepoint.com/personal/lzhang30_masonlive_gmu_edu/_layouts/15/onedrive.aspx?id=%2Fsites%2FDAEN%2D690%2DDragon%2FShared%20Documents&listurl=https%3A%2F%2Fexchangelabsgmu%2Esharepoint%2Ecom%2Fsites%2FDAEN%2D690%2DDragon%2FShared%20Documents))
            - [FL360_summary.csv](FL360_summary.csv) is the volume of ISSRs at FL360 at each datetime (hourly time).
            - [FL340_summary.csv](FL340_summary.csv) is the volume of ISSRs at FL340 at each datetime (hourly time).
            - [FL390_summary.csv](FL390_summary.csv) is the volume of ISSRs at FL390 at each datetime (hourly time).
            - [FL340_360_390_summary.csv](FL340_360_390_summary.csv) is the volume of ISSRs at the three layers(FL340, FL360, and FL390) at each datetime (hourly time).
    - [Explore.Rmd](Explore.Rmd) is the code for dashboard. Download [Explore.html](Explore.html) to see the output.
    - [Dashboard link](https://rpubs.com/long97/737625)
- **Interactive scatter plot for ISS regions at flight level FL360**
    - Run code [FL360_Cells.R](FL360_Cells.R) on [nameFile.txt](nameFile.txt) and all [Yes_CSV](https://exchangelabsgmu-my.sharepoint.com/personal/lzhang30_masonlive_gmu_edu/_layouts/15/onedrive.aspx?id=%2Fsites%2FDAEN%2D690%2DDragon%2FShared%20Documents&listurl=https%3A%2F%2Fexchangelabsgmu%2Esharepoint%2Ecom%2Fsites%2FDAEN%2D690%2DDragon%2FShared%20Documents) files to generate the records for flight level FL360.
    - Use the result in last step to make the scatter plot in Tableau.
    - [Tableau Plot](https://public.tableau.com/views/VisualizationforISSRsatFL360/VisualizationforISSRegionsatFL360from05172020to12312020?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)
   



