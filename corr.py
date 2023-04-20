# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:10:47 2023

@author: Administrator
"""

import pandas as pd
import numpy as np
import scipy
import scipy.stats

def pValue(x):
    if x < 0.001:
        x = '<0.001'
    elif x < 0.01:
        x = '<0.01'
    elif x < 0.05:
        x = '<0.05'
    elif x >= 0.05:
        x = round(x, 3)
    return x

data = pd.read_excel(".\data_combine.xlsx")
result = pd.DataFrame()
for i in range(320):
    x = data.iloc[i,1:].tolist()
    y = data.iloc[i+321,1:].tolist()
    adj = data.iloc[i,0]
    x_mean = np.mean(x)
    x_sd = np.var(x)
    y_mean = np.mean(y)
    y_sd = np.var(y)
    cor = scipy.stats.pearsonr(x, y)
    corr = cor[0]
    p = cor[1]
    list1 = [x_mean,x_sd,y_mean,y_sd,corr,p] 
    result[adj] = list1
r1 = result.T 
r1['pp'] = r1.apply(lambda x: pValue(x[5]), axis=1)
r1.to_csv('result.csv')