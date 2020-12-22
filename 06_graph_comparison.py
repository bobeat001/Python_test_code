# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 06:47:07 2020

@author: Soodong Park
"""

# 관심그룹 가져오고 데이터 시각화 하기

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import dtw

#폰트깨짐 방지
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'Malgun Gothic'

#주가 데이터 가져오기 
df_price = pd.read_csv('5years_price_data.csv', encoding='CP949').set_index('날짜')
#매출 데이터 가져오기 
df_sales = pd.read_csv('Finacial_data_매출액.csv', encoding='CP949').set_index('구분')
#영업이익 데이터 가져오기 
df_profit = pd.read_csv('Finacial_data_영업이익.csv', encoding='CP949').set_index('구분')

#관심그룹 가져오기 
df_group_sec = pd.read_csv('산업별그룹.csv', encoding='CP949').set_index('0')
df_group_theme = pd.read_csv('테마별그룹.csv', encoding='CP949').set_index('0')

#현대차 그룹 정보 가져오기
현대차그룹 = pd.read_csv('현대차그룹.csv', encoding='utf-8').rename(columns = {'0':'현대차그룹'}).drop(['Unnamed: 0'],axis=1)
현대차그룹 = list(현대차그룹['현대차그룹'])

#산업 및 테마 분류 정보 가져오기
자동차대표주 = list(df_group_theme.loc['자동차 대표주'].dropna())
자동차부품산업 = list(df_group_sec.loc['자동차부품'].dropna())
자동차부품테마 = list(df_group_theme.loc['자동차부품'].dropna())
자율주행차 = list(df_group_theme.loc['자율주행차'].dropna())
수소차 = list(df_group_theme.loc['수소차(연료전지/부품/충전소 등)'].dropna())
스마트카 = list(df_group_theme.loc['스마트카(SMART CAR)'].dropna())
타이어 = list(df_group_theme.loc['타이어'].dropna())

#관심그룹 데이터 가져오기 
#주가 정보 2016년 이후
df_현대차그룹 = df_price[현대차그룹].loc['2018-01-01':'2020-12-21']
df_자동차대표주 = df_price[자동차대표주].loc['2018-01-01':'2020-12-21']
df_자동차부품테마 = df_price[자동차부품테마].loc['2018-01-01':'2020-12-21']
#데이터 -> 변동율 변환 함수 
def change_rate(input_dataframe):
    df = input_dataframe.copy()
    for x in range(0,len(input_dataframe.columns)):
        for y in range(0,len(input_dataframe)):
            df.iloc[y,x] = 100*(input_dataframe.iloc[y,x]/input_dataframe.iloc[0,x]-1)    
    return df   
#주가 정보 변동성 추출
df_현대차그룹_변동성 = change_rate(df_현대차그룹)
df_자동차대표주_변동성 = change_rate(df_자동차대표주)
df_자동차부품테마_변동성 = change_rate(df_자동차부품테마)

#매출 정보 추출 
df_현대차그룹_매출 = df_sales[현대차그룹].loc['최근 연간 실적':'최근 연간 실적.3']
df_자동차대표주_매출 = df_sales[자동차대표주].loc['최근 연간 실적':'최근 연간 실적.3']
#매출 인덱스 이름 변경
df_현대차그룹_매출.rename(index = {'최근 연간 실적':'2017-12-31', '최근 연간 실적.1':'2018-12-31','최근 연간 실적.2':'2019-12-31', '최근 연간 실적.3':'2020-12-31'}, inplace=True)
df_자동차대표주_매출.rename(index = {'최근 연간 실적':'2017-12-31', '최근 연간 실적.1':'2018-12-31','최근 연간 실적.2':'2019-12-31', '최근 연간 실적.3':'2020-12-31'}, inplace=True)
#매출 변동성 추출
df_현대차그룹_매출_변동성 = change_rate(df_현대차그룹_매출)
df_자동차대표주_매출_변동성 = change_rate(df_자동차대표주_매출)

#영업이익 정보 추출
df_현대차그룹_영업이익 = df_profit[현대차그룹].loc['최근 연간 실적':'최근 연간 실적.3']
df_자동차대표주_영업이익 = df_profit[자동차대표주].loc['최근 연간 실적':'최근 연간 실적.3']
#영업이익 인덱스 이름 변경
df_현대차그룹_영업이익.rename(index = {'최근 연간 실적':'2017-12-31', '최근 연간 실적.1':'2018-12-31','최근 연간 실적.2':'2019-12-31', '최근 연간 실적.3':'2020-12-31'}, inplace=True)
df_자동차대표주_영업이익.rename(index = {'최근 연간 실적':'2017-12-31', '최근 연간 실적.1':'2018-12-31','최근 연간 실적.2':'2019-12-31', '최근 연간 실적.3':'2020-12-31'}, inplace=True)
#영업이익 변동성 추출
df_현대차그룹_영업이익_변동성 = change_rate(df_현대차그룹_영업이익)
df_자동차대표주_영업이익_변동성 = change_rate(df_자동차대표주_영업이익)

#주가변동성 그래프
주가변동성 = df_현대차그룹_변동성.plot.line(figsize=(10,10))
주가변동성.set_ylabel('변동율(%)')
주가변동성.set_xlabel('날짜')
주가변동성.set_title('주가변동성')
plt.show()

#매출변동성 그래프 
매출변동성 = df_현대차그룹_매출_변동성.plot.line(figsize=(10,10))
매출변동성.set_ylabel('변동율(%)')
매출변동성.set_xlabel('날짜')
매출변동성.set_title('매출변동성')
plt.show()

#영업이익변동성 그래프 
영업이익변동성 = df_현대차그룹_영업이익_변동성.plot.line(figsize=(10,10))
영업이익변동성.set_ylabel('변동율(%)')
영업이익변동성.set_xlabel('날짜')
영업이익변동성.set_title('영업이익변동성')
plt.show()

#dtw 값 추출 예시 현대차, 기아차, 현대모비스
A = '현대차'
B = '기아차'
C = '현대모비스'
AB_dtw = dtw.dtw(df_현대차그룹_변동성[A],df_현대차그룹_변동성[B], keep_internals=True).distance
AC_dtw = dtw.dtw(df_현대차그룹_변동성[A],df_현대차그룹_변동성[C], keep_internals=True).distance
BC_dtw = dtw.dtw(df_현대차그룹_변동성[B],df_현대차그룹_변동성[C], keep_internals=True).distance
AB_corr = df_현대차그룹_변동성[ [A,B] ].corr().iloc[0,1]
AC_corr = df_현대차그룹_변동성[ [A,C] ].corr().iloc[0,1]
BC_corr = df_현대차그룹_변동성[ [B,C] ].corr().iloc[0,1]
주가변동성 = df_현대차그룹_변동성[[A,B,C]].plot.line(figsize=(10,10))
주가변동성.set_ylabel('변동율(%)')
주가변동성.set_xlabel('날짜')
주가변동성.set_title('주가변동성')
주가변동성.text(0,60,A+'-'+B+'-DTW 유사도 : '+str(round(AB_dtw,1)))
주가변동성.text(0,55,A+'-'+C+'-DTW 유사도 : '+str(round(AC_dtw,1)))
주가변동성.text(0,50,B+'-'+C+'-DTW 유사도 : '+str(round(BC_dtw,1)))
주가변동성.text(0,40,A+'-'+B+'-상관계수 : '+str(round(AB_corr,2)))
주가변동성.text(0,35,A+'-'+C+'-상관계수 : '+str(round(AC_corr,2)))
주가변동성.text(0,30,B+'-'+C+'-상관계수 : '+str(round(BC_corr,2)))
plt.show()


