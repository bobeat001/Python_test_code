# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 기업 재무재표 정보 가져오기 
import pandas as pd

#기업코드 가져오기
df_stockcode = pd.read_csv('stockcode.csv',encoding='CP949').drop(columns=['Unnamed: 0'])
df_stockcode.종목코드 = df_stockcode.종목코드.map('{:06d}'.format)

#네이버금융 웹에서 재무정보 가져오기 및 저장하기
for i  in df_stockcode.index:
    
    fn_table = [1,2,3]
    name = df_stockcode.loc[i,'회사명']
    code = df_stockcode.loc[i,'종목코드']

    url_tmpl = 'http://finance.naver.com/item/main.nhn?code=%s'
    url = url_tmpl %(code)
    
    try:
        fn_table = pd.read_html(url, encoding='euc-kr')
    except ValueError:
        pass
    
    if len(fn_table) < 4:
        print("No finance table data")
    else:
        df_fn = fn_table[3]
        #재무재표 엑셀파일로 저장하기
        if len(df_fn) < 2:
            print("No csv file")
        else:
            df_fn.to_csv('%s.csv' %(name),encoding='CP949')
