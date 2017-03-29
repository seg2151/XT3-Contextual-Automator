# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:25:57 2017

@author: sgarcia
"""

from selenium import webdriver
import pandas as pd
import numpy as np
import json
from iashostlistquery import df

def get_xt3(df, URL_NUMBER=len(df)):
    driver = webdriver.Chrome()
    xt3_list = []
    hosts = df.host
    host_list = list(hosts)
    for url in host_list[:URL_NUMBER]:
        driver.get('INSERT XT3 LINK HERE{}'.format(url)) 
        json_load = json.loads(driver.find_element_by_tag_name('pre').text)
        xt3_list.append(json_load['TopChLabel'])
    driver.close()
    return xt3_list

def check_root(series_root,series_check):
    """
    Checks if every item in series_root is NOT in the corresponding item in series_check. 
    """
    bool_array = []
    if len(series_root) != len(series_check):
        return None
    else:
        for i,j in zip(series_root,series_check):
            if 'http' in i:
                i = i[7:]
            elif 'https' in i:
                i = i[8:]
            splits = i.split('.')
            if len(splits) == 2:
                bool_array.append(not splits[0] in j)
            
            elif len(splits) > 2:
                bool_array.append(not(splits[0] in j or splits[1] in j))
    return pd.Series(bool_array)

def shorten(string):
    if len(string) > 250:
        return string[:250]
    else:
        return string

shortened = df['extplacementid'].apply(shorten)
nonmatch = df[check_root(df['host'],df['extplacementid'])]      

xt3_list = get_xt3(nonmatch)
s = pd.Series(xt3_list, name = 'IAB',index=nonmatch.index)
output = pd.concat([nonmatch, s],axis=1)

