# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:56:21 2020

@author: Soodong Park
"""

#산업군, 테마군 그룹 데이터 불러오기 및 저장하기

import pandas as pd
import csv

path = 'C:/Users/Soodong Park/Documents/python_test/grouping_from_YJ/'
file_sec = 'secCmptCsvFile_20201220.csv'
file_theme = 'themeCmptCsvFile_20201220.csv'

f_sec = open(path+file_sec, mode='rt', encoding='utf-8')
reader = csv.reader(f_sec)

csv_list = []
for x in reader:
    csv_list.append(x)
f_sec.close()

df_sec = pd.DataFrame(csv_list)

f_theme = open(path+file_theme, mode='rt', encoding='utf-8')
reader = csv.reader(f_theme)

csv_list = []
for x in reader:
    csv_list.append(x)
f_theme.close()

df_theme = pd.DataFrame(csv_list)
    
df_sec.set_index(0, inplace=True)
df_theme.set_index(0, inplace=True)

df_sec.to_csv('산업별그룹.csv', encoding='CP949')
df_theme.to_csv('테마별그룹.csv', encoding='CP949')




