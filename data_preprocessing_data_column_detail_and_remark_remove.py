import pandas as pd

# CSV 파일 읽기
df1 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세정보비고병합_데이터1.csv", encoding='utf-8')
df2 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세정보비고병합_데이터2.csv", encoding='utf-8')
df3 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세정보비고병합_데이터3.csv", encoding='utf-8')

# 필요 없는 열 제거 (구분, 업체명, 고시번호, 고시일자)
df_cleaned1 = df1.drop([ '상세정보','비고'], axis=1)
df_cleaned2 = df2.drop([ '상세정보','비고'], axis=1)
df_cleaned3 = df3.drop([ '상세정보','비고'], axis=1)


# 전처리된 데이터를 저장
df_cleaned1.to_csv('상세정보비고병합 및 상세정보제거 비고제거_데이터1.csv', index=False, encoding='utf-8-sig')
df_cleaned2.to_csv('상세정보비고병합 및 상세정보제거 비고제거_데이터2.csv', index=False, encoding='utf-8-sig')
df_cleaned3.to_csv('상세정보비고병합 및 상세정보제거 비고제거_데이터3.csv', index=False, encoding='utf-8-sig')
