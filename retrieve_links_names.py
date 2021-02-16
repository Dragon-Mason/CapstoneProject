#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:18:04 2021

@author: longzhang
"""

import requests
from bs4 import BeautifulSoup
import json

# 1. Request, catch response, and extract response as html: html_doc
url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/'
r = requests.get(url) 
html_doc = r.text


# 2. get the hyperlinks of the folders for months from 202011 to 202101
soup = BeautifulSoup(html_doc) # Parsing HTML with BeautifulSoup
a_tags = soup.find_all('a') # Find all 'a' tags (which define hyperlinks): a_tags
month_urls = [] # a list to store links
for link in a_tags:
    month_urls.extend([url+link.get('href')])
month_urls = month_urls[-4:-1] # Only Keep the hyperlinks of the folders from 202011 to 202101
# month_urls



# 3. get the hyperlinks of the folders for days in the three months
day_urls = []
for month_url in month_urls:
    r = requests.get(month_url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc)
    a_tags = soup.find_all('a')
    for link in a_tags[5:]: 
        # drop the first 5 links using a_tags[5:] since they are not links for folders of the days in those months
        day_urls.extend([month_url+link.get('href')])
# day_urls




# 4. get the hyperlinks of all grib2 and inv files in the three months
# This step will take some time
grib_inv_urls = [] # links of files
grib_inv_names = [] # names of files
for day_url in day_urls:
    r = requests.get(day_url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc)
    a_tags = soup.find_all('a')
    for link in a_tags[5:]: 
        # drop the first 5 links using a_tags[5:] since they are not links for files
        grib_inv_urls.extend([day_url+link.get('href')])
        grib_inv_names.extend([link.get('href')])
# grib_inv_urls
# grib_inv_names




# 5. get the hyperlinks of all grib2 files in the three months
grib_urls = []
grib_names = []
for i in range(len(grib_inv_urls)):
    # drop links for .inv files
    if i%2 == 0:
        grib_urls.extend([grib_inv_urls[i]])
        grib_names.extend([grib_inv_names[i]])
# grib_urls 
# grib_names


# 6. Address issues in grib_urls and grib_names 
        
# 2020/11/12 9:00 ---- file of +001 is missing
# 2020/12/11 19:00 ---- file of +000 is missing
# So, drop:
# 2020/11/12 9:00 ---- file of +000
# 2020/12/11 19:00 ---- file of +001
# 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/202011/20201112/rap_252_20201112_0900_000.grb2'
# 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/202012/20201211/rap_252_20201211_1900_001.grb2'
# 'rap_252_20201112_0900_000.grb2'
# 'rap_252_20201211_1900_001.grb2'
url1 = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/202011/20201112/rap_252_20201112_0900_000.grb2'
url2 = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/202012/20201211/rap_252_20201211_1900_001.grb2'
name1 = 'rap_252_20201112_0900_000.grb2'
name2 = 'rap_252_20201211_1900_001.grb2'
grib_urls_drop = []
grib_names_drop = []
for i in range(len(grib_urls)):
    if (grib_urls[i] != url1) and (grib_urls[i] != url2):
        grib_urls_drop.extend([grib_urls[i]])
        grib_names_drop.extend([grib_names[i]])
len(grib_urls) # 4366
len(grib_urls_drop) # 4364

# drop links for +001 files
grib_urls_000 = []
grib_names_000 = []
for i in range(len(grib_urls_drop)):
    # drop links for .inv files
    if i%2 == 0:
        grib_urls_000.extend([grib_urls_drop[i]])
        grib_names_000.extend([grib_names_drop[i]])

# add the file of 2020/11/12 9:00 +000
grib_urls_000.extend([url1])
grib_names_000.extend([name1])
len(grib_urls_000) # 2183

# add the file of 2020/12/11 18:00 +001 as the file of 2020/12/11 19:00 +000
url3 = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/202012/20201211/rap_252_20201211_1800_001.grb2'
name3 = 'rap_252_20201211_1900_000.grb2'
grib_urls_000.extend([url3])
grib_names_000.extend([name3])
len(grib_urls_000) # 2183

# 7. Export files
with open('grib_urls.txt', 'w') as f:
    f.write(json.dumps(grib_urls_000))
with open('grib_names.txt', 'w') as f:
    f.write(json.dumps(grib_names_000))


 
  
    
    
    
    
    