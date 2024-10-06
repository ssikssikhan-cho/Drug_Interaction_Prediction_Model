import pandas as pd

# 파일 읽기 (경로는 필요에 따라 수정)
df1 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세정보비고병합 및 상세정보제거 비고제거_데이터1.csv", encoding='utf-8')
df2 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세정보비고병합 및 상세정보제거 비고제거_데이터2.csv", encoding='utf-8')
df3 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세정보비고병합 및 상세정보제거 비고제거_데이터3.csv", encoding='utf-8')

# 중복된 값이 있는 행을 찾아 제거 (중복 기준: 성분명A, 성분코드A, 성분명B, 성분코드B, 상세_비고_병합)
df_cleaned1 = df1.drop_duplicates(subset=['성분명A', '성분코드A', '성분명B', '성분코드B', '상세_비고_병합'])
df_cleaned2 = df2.drop_duplicates(subset=['성분명A', '성분코드A', '성분명B', '성분코드B', '상세_비고_병합'])
df_cleaned3 = df3.drop_duplicates(subset=['성분명A', '성분코드A', '성분명B', '성분코드B', '상세_비고_병합'])


# 병합된 데이터를 새로운 파일로 저장
df_cleaned1.to_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\중복제거_데이터1.csv', index=False, encoding='utf-8-sig')
df_cleaned2.to_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\중복제거_데이터2.csv', index=False, encoding='utf-8-sig')
df_cleaned3.to_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\중복제거_데이터3.csv', index=False, encoding='utf-8-sig')
