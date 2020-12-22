# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 02:00:59 2020

@author: -
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas
import datetime

#기업코드 가져오기
df_stockcode = pd.read_csv('stockcode.csv',encoding='CP949').drop(columns=['Unnamed: 0'])
df_stockcode.종목코드 = df_stockcode.종목코드.map('{:06d}'.format)

# 기업 주가 정보 가져오기
def naver_get_stock_price(코드, 년수):
    
    오늘날짜 = datetime.datetime.now() #현재 날짜 가져오기
    #period = float(년수) * 365
    가져올기간 = float(년수) * 365 / 1.47
    네이버주소 = f'http://fchart.stock.naver.com/sise.nhn?symbol={코드}&timeframe=day&count={가져올기간}&requestType=0'
    request_result = requests.get(네이버주소)
    bs = BeautifulSoup(request_result.content, 'html.parser')
    all_data = bs.select('chartdata')
    종목명 = all_data[0].attrs['name']
    주가데이터 = bs.select('item')    
    데이터_dict = {}    
    날짜_list = []
    수정종가_list = []
    for i in range(len(주가데이터)):
        int = str(주가데이터[i])[12:-9]
        int_splited = int.split('|')
        날짜 = pandas.to_datetime(int_splited[0])
        수정종가 = float(int_splited[4])
        날짜_list.append(날짜)
        수정종가_list.append(수정종가)        
    
    데이터_dict[f'{종목명}'] = 수정종가_list
  
    df = pandas.DataFrame(데이터_dict,날짜_list)
    df.reset_index(inplace = True)
    df = df.rename({'index':'날짜'}, axis=1)
    
    print(df)
    file_name = f'{종목명}_{str(날짜_list[0])[:10]}-{str(오늘날짜)[:10]}'
    df.to_csv('{0}.csv'.format(file_name), encoding='CP949')
    print('\n{0} 저장완료'.format(file_name))
    

for i  in df_stockcode.index:
    
    fn_table = [1,2,3]
    name = df_stockcode.loc[i,'회사명']
    code = df_stockcode.loc[i,'종목코드']
    
    try:
        naver_get_stock_price(code,'5')
    except: #IndexError:
        pass
    



    
    


    

    