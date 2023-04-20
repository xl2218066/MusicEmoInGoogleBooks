# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:39:17 2021

@author: 313
"""
import time
from selenium import webdriver
import pandas as pd
import re

adj = pd.read_csv(".\adj.csv")#the list of adjectives
adj.head()
adjname = adj.iloc[:,0]
df = pd.DataFrame(index=adjname.index)
driver = webdriver.Chrome()
time0 = time.time()
target_list = ['music']
for target in target_list:
    df = pd.DataFrame(index=adjname.index)
    for num, adj in  enumerate(adjname):
        driver.get('https://books.google.com/ngrams/graph?content=&year_start=1800&year_end=2012&corpus=15&smoothing=0&share=&direct_url=')#corpus=17, American English 2012; corpus=18, British English; corpus=15, English; corpus=16, English Fiction  
        time.sleep(30)
        search_box = driver.find_element_by_name('content')
        search_box.send_keys('{} {}'.format(adj,target) ) # An example of the word "child".
        #search_box.send_keys('music') # target
        search_box.submit()        
        result = re.findall(r'", "timeseries": \[(.*?)\]\}',driver.page_source, re.M)
        df.loc[num,"Adjname"]=adj
        df.loc[num,"results"] = ', '.join(result) 
    time.sleep(10)
    driver.quit()
    print(time.time()-time0)
    a=pd.merge(df,pd.DataFrame(df['results'].str.split(', ',expand=True)),how='left',left_index=True,right_index=True)
    a.fillna(0,inplace =True)
    a.to_csv('data.csv')

