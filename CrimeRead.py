#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:37:50 2019

@author: christophergsell
"""

import pandas as pd


my_data = pd.read_csv('CrimeData.csv', delimiter=';', usecols = ['Date of Occurrence', 'latitude_longitude'], skip_blank_lines = True)
test = pd.DataFrame(my_data)
test = test.dropna()
test.sort_values('Date of Occurrence')

pd.to_datetime(test['Date of Occurrence'])

test[['latitude','longitude']] = test['latitude_longitude'].str.split(',', expand=True)
test = test.drop(['latitude_longitude'],axis=1)
print(len(test.columns))
print(test)


#currating to just Northside Chapel Hill
#latitude coordinates
y = [35.909789, 35.916219, 35.920216, 35.918408, 35.914168]
#longitude coordinates
x = [-79.069138, -79.069438, -79.063473, -79.058967, -79.056263]
for i in range(test['Date of Occurrence'].size):
    if test['longitude'][i] >= x[0] & test['longitude'][i] < x[1]:
       if test['longitude'][i] 
    elif 
        

#From 2010-2014
first_sample = test[(test['Date of Occurrence'] >= '2010-01-01') & (test['Date of Occurrence'] < '2014-01-01')]
crimes1 = first_sample['Date of Occurrence'].size
#From 2014-2018
second_sample = test[(test['Date of Occurrence'] >= '2014-01-01') & (test['Date of Occurrence'] < '2018-01-01')]
crimes2 = second_sample['Date of Occurrence'].size