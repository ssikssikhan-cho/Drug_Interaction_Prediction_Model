import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import numpy as np

# 새로운 레이블을 처리하기 위한 함수 정의
def handle_unseen_labels(le, new_labels):
    """
    LabelEncoder가 새로운 레이블을 처리할 수 있도록 기존 레이블에 새로운 레이블을 추가하는 함수.
    
    Parameters:
    - le: 학습된 LabelEncoder 객체
    - new_labels: 새로운 데이터에서 등장하는 레이블 리스트
    
    Returns:
    - le: 새로운 레이블이 포함된 LabelEncoder 객체
    """
    # 기존 레이블에 없는 새로운 레이블을 찾아 추가
    new_classes = np.append(le.classes_, np.setdiff1d(new_labels, le.classes_))
    
    # LabelEncoder 객체에 새로운 클래스 할당
    le.classes_ = new_classes
    return le

# 1. 데이터 로드 (파일 A와 파일 B)
data = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\매치 데스트1.csv", encoding='utf-8')
data_null = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\중복제거_데이터2.csv", encoding='utf-8')

# 2. 필요한 열만 추출 (성분명, 성분코드, 질병_정규화)
data = data[['성분명A', '성분코드A', '성분명B', '성분코드B', '질병_정규화']]
data_null = data_null[['성분명A', '성분코드A', '성분명B', '성분코드B']]  # 질병_정규화 제외

# 3. 레이블 인코딩 (성분명과 성분코드 범주형 데이터 수치화)
le_name_a = LabelEncoder()
le_name_b = LabelEncoder()
le_code_a = LabelEncoder()
le_code_b = LabelEncoder()
le_disease = LabelEncoder()

# 각 성분명과 성분코드에 대해 별도의 인코딩 (파일 A에 대해 fit)
data['성분명A'] = le_name_a.fit_transform(data['성분명A'])
data['성분코드A'] = le_code_a.fit_transform(data['성분코드A'])
data['성분명B'] = le_name_b.fit_transform(data['성분명B'])
data['성분코드B'] = le_code_b.fit_transform(data['성분코드B'])
data['질병_정규화'] = le_disease.fit_transform(data['질병_정규화'])

# 4. 파일 B에도 동일한 인코더 사용해 인코딩 (새로운 레이블 처리)
le_name_a = handle_unseen_labels(le_name_a, data_null['성분명A'])
le_code_a = handle_unseen_labels(le_code_a, data_null['성분코드A'])
le_name_b = handle_unseen_labels(le_name_b, data_null['성분명B'])
le_code_b = handle_unseen_labels(le_code_b, data_null['성분코드B'])

data_null['성분명A'] = le_name_a.transform(data_null['성분명A'])
data_null['성분코드A'] = le_code_a.transform(data_null['성분코드A'])
data_null['성분명B'] = le_name_b.transform(data_null['성분명B'])
data_null['성분코드B'] = le_code_b.transform(data_null['성분코드B'])

# 5. 파일 A의 입력(X)와 출력(y) 데이터 설정
X = data[['성분명A', '성분코드A', '성분명B', '성분코드B']]
y = data['질병_정규화']

# 6. 데이터셋 분리 (훈련, 테스트 세트)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. SMOTE 적용 (소수 클래스 증강, k_neighbors 값 설정)
smote = SMOTE(random_state=42, k_neighbors=1)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# 8. GridSearchCV를 사용하여 Random Forest의 최적의 하이퍼파라미터 탐색
param_grid = {
    'n_estimators': [100, 200, 300],  # 하이퍼파라미터 범위 설정
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train_resampled, y_train_resampled)

# 9. 최적의 모델로 테스트 데이터 예측
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# 10. 성능 평가 (파일 A에 대해)
unique_labels = y_test.unique()
print(classification_report(y_test, y_pred, labels=unique_labels, target_names=le_disease.inverse_transform(unique_labels), zero_division=1))

# 11. 파일 B에 대해서도 예측 수행 (타겟 변수 없이)
X_b = data_null[['성분명A', '성분코드A', '성분명B', '성분코드B']]  # 질병_정규화는 포함하지 않음
predicted_disease_b = best_model.predict(X_b)

# 예측된 결과를 원래 데이터로 변환
data_null['질병_정규화'] = le_disease.inverse_transform(predicted_disease_b)

# 12. 결합된 파일 B 데이터 저장
data_null.to_csv('predicted_data_b.csv', index=False, encoding='utf-8-sig')
print("파일 B에 대한 예측 결과가 저장되었습니다.")
