import pandas as pd

df1 = pd.read_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\의약품안전사용서비스(DUR)_병용금기 품목리스트 2020.9.csv', encoding='cp949')
df2 = pd.read_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\의약품안전사용서비스(DUR)_병용금기 품목리스트 2022.6.csv', encoding='cp949')
df3 = pd.read_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\의약품안전사용서비스(DUR)_병용금기 품목리스트 2023.5.csv', encoding='cp949')

# 변환된 파일 저장
df1.to_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR)_병용금기_변환된_2020.9.csv', index=False, encoding='utf-8-sig')
df2.to_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR)_병용금기_변환된_2022.6.csv', index=False, encoding='utf-8-sig')
df3.to_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR)_병용금기_변환된_2023.5.csv', index=False, encoding='utf-8-sig')

print("파일이 변환되어 저장되었습니다.")
