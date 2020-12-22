# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:51:07 2020

@author: Soodong Park
"""

import pandas as pd
import csv
import glob
import os

# 주가정보 종합 데이터프레임 만들기
path = 'C:/Users/Soodong Park/Documents/python_test/기업주가분석_연습/주가정보/'

csv_files = glob.glob(path+'*.csv')
df_price_total = pd.DataFrame(columns=['날짜'])

for index,value in enumerate(csv_files):    
    df = pd.read_csv(csv_files[index],encoding='CP949')
    df = df.drop(columns=['Unnamed: 0'])
    df_price_total = pd.merge(df_price_total,df,how='outer', on='날짜')
    
df_price_total.set_index('날짜',drop=True, append=False, inplace = True)
df_price_total.sort_index(ascending=True, inplace = True)

# 주가정보 종합 데이터프레임 저장하기
df_price_total.to_csv('5years_price_data.csv', encoding='CP949')


# 재무정보 매출액 종합 데이터프레임 만들기
path = 'C:/Users/Soodong Park/Documents/python_test/기업주가분석_연습/재무정보/'

csv_files = glob.glob(path+'*.csv')
df_sales_total = pd.DataFrame(columns=['구분'])

for index,value in enumerate(csv_files):    
    df = pd.read_csv(csv_files[index],encoding='CP949')
    if len(df.index) > 12:
        df = df.drop(columns=['Unnamed: 0']).drop([1]).set_index('주요재무정보')
        df = df.transpose()
        df = df.reset_index()
        df = df.rename(columns={'index':'구분'}) 
        df = df.loc[:,['구분','매출액']] 
        name = os.path.basename(os.path.normpath(csv_files[index]))
        df = df.rename(columns={'매출액':name[:-4]}) 
        df_sales_total = pd.merge(df_sales_total,df,how='outer', on='구분')
    else:
        print('No data')
        
df_sales_total.set_index('구분',drop=True, append=False, inplace = True)
df_sales_total.rename(columns = {'현대자동차':'현대차','기아자동차':'기아차','쌍용자동차':'쌍용차'}, inplace=True)
df_sales_total.to_csv('Finacial_data_매출액.csv', encoding='CP949')


# 재무정보 영업이익 종합 데이터프레임 만들기
path = 'C:/Users/Soodong Park/Documents/python_test/기업주가분석_연습/재무정보/'
csv_files = glob.glob(path+'*.csv')
df_profit_total = pd.DataFrame(columns=['구분'])

for index,value in enumerate(csv_files):    
    df = pd.read_csv(csv_files[index],encoding='CP949')
    if len(df.index) > 12:
        df = df.drop(columns=['Unnamed: 0']).drop([1]).set_index('주요재무정보')
        df = df.transpose()
        df = df.reset_index()
        df = df.rename(columns={'index':'구분'}) 
        df = df.loc[:,['구분','영업이익']] 
        name = os.path.basename(os.path.normpath(csv_files[index]))
        df = df.rename(columns={'영업이익':name[:-4]}) 
        df_profit_total = pd.merge(df_profit_total,df,how='outer', on='구분')
    else:
        print('No data')
        
df_profit_total.set_index('구분',drop=True, append=False, inplace = True)
df_profit_total.rename(columns = {'현대자동차':'현대차','기아자동차':'기아차','쌍용자동차':'쌍용차'}, inplace=True)
df_profit_total.to_csv('Finacial_data_영업이익.csv', encoding='CP949')


