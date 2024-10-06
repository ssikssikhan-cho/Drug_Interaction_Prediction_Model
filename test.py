import pandas as pd

# 파일 읽기 (데이터가 있는 csv 파일 경로 입력)
df1 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\중복제거_데이터1.csv", encoding='utf-8')
df2 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\중복제거_데이터2.csv", encoding='utf-8')
df3 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\중복제거_데이터3.csv", encoding='utf-8')

# 특정 열 추출 (예를 들어 '제품명' 열을 추출)
extracted_column1 = df1['상세_비고_병합']
extracted_column2 = df2['상세_비고_병합']
extracted_column3 = df3['상세_비고_병합']

# 중복 값 제거
unique_values1 = extracted_column1.drop_duplicates()
unique_values2 = extracted_column2.drop_duplicates()
unique_values3 = extracted_column3.drop_duplicates()
# 중복 제거된 값들을 새로운 DataFrame으로 변환
unique_df1 = pd.DataFrame(unique_values1)
unique_df2 = pd.DataFrame(unique_values2)
unique_df3 = pd.DataFrame(unique_values3)

# 중복 제거된 데이터 엑셀 파일로 저장
unique_df1.to_csv('상세_비고_병합만 중복제거_데이터1.csv', index=False, encoding='utf-8-sig')
unique_df2.to_csv('상세_비고_병합만 중복제거_데이터2.csv', index=False, encoding='utf-8-sig')
unique_df3.to_csv('상세_비고_병합만 중복제거_데이터3.csv', index=False, encoding='utf-8-sig')
