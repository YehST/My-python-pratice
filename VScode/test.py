import requests as rq  # 載入requests套件, 縮寫rq
import csv  # 載入CSV套件, 以處理CSV格式
import pandas as pd  # 載入pandas套件, 縮寫pd

url = 'http://www.twse.com.tw/exchangeReport/BWIBBU_ALL?response=open_data'
r = rq.request('GET', url)
data = list(csv.reader(r.text.split('\n'), delimiter=','))
df = pd.DataFrame(data[1:], columns=['股票代號', '股票名稱', '本益比', '殖利率(%)', '股價淨值比'])
df = df.dropna()
df['本益比'] = df['本益比'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['本益比'] = df['本益比'].astype(float)
df['殖利率(%)'] = df['殖利率(%)'].apply(pd.to_numeric, errors='coerce').fillna(0.0)
df['殖利率(%)'] = df['殖利率(%)'].astype(float)
mask1 = df['本益比'] > 0.1
mask2 = df['本益比'] < 8.0
mask3 = df['殖利率(%)'] > 8.0
df1 = df[(mask1 & mask2 & mask3)]
print(df1)
