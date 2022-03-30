# -*- coding: utf-8 -*-

# 라이브러리 불러오기
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# 위키피디아 미국 ETF 웹 페이지에서 필요한 정보를 스크래핑하여 딕셔너리 형태로 변수 etfs에 저장
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')   
rows = soup.select('div > ul > li')
    
etfs = {}
for row in rows:

    try:
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = ['NYSE Arca']
        etf_ticker = re.findall('\(NYSE Arca(.*)\s(.*)\)', row.text.replace(u'\xa0', u' '))
        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            etfs[etf_ticker[0][1]] = [etf_market[0], etf_name[0]]


    except AttributeError as err:
        pass    

# etfs 딕셔너리 출력
print(etfs)
print('\n')

# etfs 딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(etfs)
print(df)

# df2 = df.transpose()
# df2.colums=['etf_market','etf_name']
# df2.rename(index = {"" : 'etf_ticker'})
# print(df2)


df2 = df.transpose()
df2.columns = ['etf_market', 'etf_name']
df2.rename(index = {"" : "eft_ticker"})
print(df2)