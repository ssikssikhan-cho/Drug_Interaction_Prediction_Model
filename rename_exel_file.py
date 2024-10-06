import pandas as pd

df=pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\predicted_data_b.csv", encoding='utf-8-sig')
df.to_csv('predicted_data_b.csv',index=False, encoding='utf-8-sig')