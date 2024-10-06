import pandas as pd

# 2. 엑셀 A와 B 파일을 데이터프레임으로 읽어옵니다.
df_a = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\중복제거_데이터3.csv" # 엑셀 A의 파일 경로
                   , encoding='utf-8-sig')  # 엑셀 A 파일
df_b = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세_비고_병합만 중복제거_데이터1.csv"  # 엑셀 B의 파일 경로
                   , encoding='utf-8-sig')  # 엑셀 B 파일

# 3. 엑셀 B 파일에 '상세_비고_병합'과 '질병_정규화'가 포함되어 있다고 가정합니다.
# 엑셀 A와 엑셀 B를 '상세_비고_병합' 컬럼을 기준으로 병합합니다.
merged_df = pd.merge(df_a, df_b[['상세_비고_병합', '질병_정규화']], on="상세_비고_병합", how="left")

# 4. 결과를 새로운 엑셀 파일로 저장합니다.  # 병합 결과를 저장할 파일 경로
merged_df.to_csv('매치 데스트3.csv',index=False, encoding='utf-8-sig')