# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:10:54 2023

@author: Administrator
"""

import pandas as pd

path = ".\googlebooks-eng-all-1gram-20120701-m.txt" # data can be downloaded at https://storage.googleapis.com/books/ngrams/books/datasetsv3.html 
n = 0
row = []
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        if 'music' in line:
            row.append(line)    
data = pd.DataFrame(row)
data.columns = ['raw']        
data['word'] = data['raw'].map(lambda x:x.split('\t')[0])   
data['year'] = data['raw'].map(lambda x:x.split('\t')[1])
data['match_count'] = data['raw'].map(lambda x:x.split('\t')[2])
data['volume_count'] = data['raw'].map(lambda x:x.split('\t')[3]) 
df_music = data.loc[data['word'] == 'music', :] 
df_music.to_csv('music_word_count.csv')           