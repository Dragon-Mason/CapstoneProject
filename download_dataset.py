# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:47:10 2021

@author: iwanJ
"""

import urllib.request
import os
os.chdir('D:/George Mason University/5. Spring 2021/DAEN 690/Dataset')
os.getcwd()

f = open("linkFile.txt", "w")
f.close()
f = open("nameFile.txt", "w")
f.close()
  
for x in range(202008, 202013):        
    if (x % 2 == 0):
        for j in range(1, 32):
            for k in range(0, 24):
                if ((x == 202012) & (j == 11) & (k == 19)):
                    url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/202012/20201211/rap_252_20201211_1800_001.grb2'
                    print(url)
                    f = open("linkFile.txt", "a")
                    f.write(url)
                    f.write('\n')
                    f.close()
                    urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2')
                    f = open("nameFile.txt", "a")
                    f.write('rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2\n')
                    f.close()
                else:
                    if (j < 10):
                        if (k < 10):
                            url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + '0' + str(j) + '/' + 'rap_252_' + str(x) + '0' + str(j) + '_0' + str(k) + '00_000.grb2'
                            print(url)
                            f = open("linkFile.txt", "a")
                            f.write(url)
                            f.write('\n')
                            f.close()
                            urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + '0' + str(j) + '_0' + str(k) + '00_000.grb2')
                            f = open("nameFile.txt", "a")
                            f.write('rap_252_' + str(x) + '0' + str(j) + '_0' + str(k) + '00_000.grb2\n')
                            f.close()
                        else:
                            url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + '0' + str(j) + '/' + 'rap_252_' + str(x) + '0' + str(j) + '_' + str(k) + '00_000.grb2'
                            print(url)
                            f = open("linkFile.txt", "a")
                            f.write(url)
                            f.write('\n')
                            f.close()
                            urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + '0' + str(j) + '_' + str(k) + '00_000.grb2')
                            f = open("nameFile.txt", "a")
                            f.write('rap_252_' + str(x) + '0' + str(j) + '_' + str(k) + '00_000.grb2\n')
                            f.close()
                    else:
                        if (k < 10):
                            url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + str(j) + '/' + 'rap_252_' + str(x) + str(j) + '_0' + str(k) + '00_000.grb2'
                            print(url)
                            f = open("linkFile.txt", "a")
                            f.write(url)
                            f.write('\n')
                            f.close()
                            urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + str(j) + '_0' + str(k) + '00_000.grb2')
                            f = open("nameFile.txt", "a")
                            f.write('rap_252_' + str(x) + str(j) + '_0' + str(k) + '00_000.grb2\n')
                            f.close()
                        else:
                            url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + str(j) + '/' + 'rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2'
                            print(url)
                            f = open("linkFile.txt", "a")
                            f.write(url)
                            f.write('\n')
                            f.close()
                            urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2')
                            f = open("nameFile.txt", "a")
                            f.write('rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2\n')
                            f.close()
    else:
        for j in range(1, 31):
            for k in range(0, 24):
                if (j < 10):
                    if (k < 10):
                        url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + '0' + str(j) + '/' + 'rap_252_' + str(x) + '0' + str(j) + '_0' + str(k) + '00_000.grb2'
                        print(url)
                        f = open("linkFile.txt", "a")
                        f.write(url)
                        f.write('\n')
                        f.close()
                        urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + '0' + str(j) + '_0' + str(k) + '00_000.grb2')
                        f = open("nameFile.txt", "a")
                        f.write('rap_252_' + str(x) + '0' + str(j) + '_0' + str(k) + '00_000.grb2\n')
                        f.close()
                    else:
                        url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + '0' + str(j) + '/' + 'rap_252_' + str(x) + '0' + str(j) + '_' + str(k) + '00_000.grb2'
                        print(url)
                        f = open("linkFile.txt", "a")
                        f.write(url)
                        f.write('\n')
                        f.close()
                        urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + '0' + str(j) + '_' + str(k) + '00_000.grb2')
                        f = open("nameFile.txt", "a")
                        f.write('rap_252_' + str(x) + '0' + str(j) + '_' + str(k) + '00_000.grb2\n')
                        f.close()
                else:
                    if (k < 10):
                        url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + str(j) + '/' + 'rap_252_' + str(x) + str(j) + '_0' + str(k) + '00_000.grb2'
                        print(url)
                        f = open("linkFile.txt", "a")
                        f.write(url)
                        f.write('\n')
                        f.close()
                        urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + str(j) + '_0' + str(k) + '00_000.grb2')
                        f = open("nameFile.txt", "a")
                        f.write('rap_252_' + str(x) + str(j) + '_0' + str(k) + '00_000.grb2\n')
                        f.close()
                    else:
                        url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + str(j) + '/' + 'rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2'
                        print(url)
                        f = open("linkFile.txt", "a")
                        f.write(url)
                        f.write('\n')
                        f.close()
                        urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2')
                        f = open("nameFile.txt", "a")
                        f.write('rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2\n')
                        f.close()

for x in range(202101, 202102):
    for j in range(1, 31):
        for k in range(0, 24):
            if (j < 10):
                if (k < 10):
                    url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + '0' + str(j) + '/' + 'rap_252_' + str(x) + '0' + str(j) + '_0' + str(k) + '00_000.grb2'
                    print(url)
                    f = open("linkFile.txt", "a")
                    f.write(url)
                    f.write('\n')
                    f.close()
                    urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + '0' + str(j) + '_0' + str(k) + '00_000.grb2')
                    f = open("nameFile.txt", "a")
                    f.write('rap_252_' + str(x) + '0' + str(j) + '_0' + str(k) + '00_000.grb2\n')
                    f.close()
                else:
                    url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + '0' + str(j) + '/' + 'rap_252_' + str(x) + '0' + str(j) + '_' + str(k) + '00_000.grb2'
                    print(url)
                    f = open("linkFile.txt", "a")
                    f.write(url)
                    f.write('\n')
                    f.close()
                    urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + '0' + str(j) + '_' + str(k) + '00_000.grb2')
                    f = open("nameFile.txt", "a")
                    f.write('rap_252_' + str(x) + '0' + str(j) + '_' + str(k) + '00_000.grb2\n')
                    f.close()
            else:
                if (k < 10):
                    url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + str(j) + '/' + 'rap_252_' + str(x) + str(j) + '_0' + str(k) + '00_000.grb2'
                    print(url)
                    f = open("linkFile.txt", "a")
                    f.write(url)
                    f.write('\n')
                    f.close()
                    urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + str(j) + '_0' + str(k) + '00_000.grb2')
                    f = open("nameFile.txt", "a")
                    f.write('rap_252_' + str(x) + str(j) + '_0' + str(k) + '00_000.grb2\n')
                    f.close()
                else:
                    url = 'https://www.ncei.noaa.gov/data/rapid-refresh/access/rap-252-20km/analysis/' + str(x) + '/' + str(x) + str(j) + '/' + 'rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2'
                    print(url)
                    f = open("linkFile.txt", "a")
                    f.write(url)
                    f.write('\n')
                    f.close()
                    urllib.request.urlretrieve(url, 'D:/George Mason University/5. Spring 2021/DAEN 690/Dataset/rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2')
                    f = open("nameFile.txt", "a")
                    f.write('rap_252_' + str(x) + str(j) + '_' + str(k) + '00_000.grb2\n')
                    f.close()
                    