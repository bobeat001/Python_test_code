# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:49:23 2020

@author: Soodong Park
"""

#기업이름 및 종목번호 가져오기
import pandas as pd

stockcode = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download')
df_stockcode = stockcode[0]

#종목코드의 숫자값을 6자리 문자열로 설정하기 빈자리 0채우기
df_stockcode.종목코드 = df_stockcode.종목코드.map('{:06d}'.format)
df_stockcode = df_stockcode[['회사명','종목코드']]    

for i  in df_stockcode.index:
    
    fn_table = [1,2,3]
    name = df_stockcode.loc[i,'회사명']
    code = df_stockcode.loc[i,'종목코드']
    
    try:
        naver_get_stock_price(code,'5')
    except: #IndexError:
        pass
    
# 저장하기    
df_stockcode.to_csv('stockcode.csv',encoding='CP949')
