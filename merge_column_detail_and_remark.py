import pandas as pd

# 파일 읽기
df1 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\열제거_데이터1.csv", encoding='utf-8-sig')
df2 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\열제거_데이터2.csv", encoding='utf-8-sig')
df3 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\열제거_데이터3.csv", encoding='utf-8-sig')

# 비고와 상세정보 열을 병합
df1['상세_비고_병합'] = df1.apply(lambda row: f"{row['상세정보']}, {row['비고']}" if pd.notnull(row['상세정보']) and pd.notnull(row['비고']) else row['상세정보'] if pd.notnull(row['상세정보']) else row['비고'], axis=1)
df2['상세_비고_병합'] = df2.apply(lambda row: f"{row['상세정보']}, {row['비고']}" if pd.notnull(row['상세정보']) and pd.notnull(row['비고']) else row['상세정보'] if pd.notnull(row['상세정보']) else row['비고'], axis=1)
df3['상세_비고_병합'] = df3.apply(lambda row: f"{row['상세정보']}, {row['비고']}" if pd.notnull(row['상세정보']) and pd.notnull(row['비고']) else row['상세정보'] if pd.notnull(row['상세정보']) else row['비고'], axis=1)
# 결과 확인

# 병합 후 데이터 저장
df1.to_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세정보비고병합_데이터1.csv', index=False, encoding='utf-8-sig')
df2.to_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세정보비고병합_데이터2.csv', index=False, encoding='utf-8-sig')
df3.to_csv('C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세정보비고병합_데이터3.csv', index=False, encoding='utf-8-sig')