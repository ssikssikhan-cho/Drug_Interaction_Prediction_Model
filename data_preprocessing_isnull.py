import pandas as pd

# 파일 목록
file_names = ['매치 데스트1.csv', '매치 데스트2.csv', '매치 데스트3.csv']

# 각 파일을 처리하고 결측치가 있는지 확인
for file_name in file_names:
    # 파일 읽기
    df = pd.read_csv(f'C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\{file_name}', encoding='utf-8-sig')

    # 각 열의 결측치 개수 확인
    missing_data = df.isnull().sum()

    # 결과 출력
    print(f'파일명: {file_name}')
    print(missing_data)
    print('-' * 40)