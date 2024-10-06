import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import joblib

# 1. 데이터 로드
data = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\매치 데스트1.csv", encoding='utf-8')

# 2. 필요한 열만 추출 (성분명, 성분코드, 질병_정규화)
data = data[['성분명A', '성분코드A', '성분명B', '성분코드B', '질병_정규화']]

# 3. 레이블 인코딩 (성분명과 성분코드 범주형 데이터 수치화)
le_name_a = LabelEncoder()
le_name_b = LabelEncoder()
le_code_a = LabelEncoder()
le_code_b = LabelEncoder()
le_disease = LabelEncoder()

# 각 성분명과 성분코드에 대해 별도의 인코딩
data['성분명A'] = le_name_a.fit_transform(data['성분명A'])
data['성분코드A'] = le_code_a.fit_transform(data['성분코드A'])
data['성분명B'] = le_name_b.fit_transform(data['성분명B'])
data['성분코드B'] = le_code_b.fit_transform(data['성분코드B'])
data['질병_정규화'] = le_disease.fit_transform(data['질병_정규화'])

# 4. 입력(X)와 출력(y) 데이터 설정
X = data[['성분명A', '성분코드A', '성분명B', '성분코드B']]
y = data['질병_정규화']

# 5. 데이터셋 분리 (훈련, 테스트 세트)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. SMOTE 적용 (소수 클래스 증강, k_neighbors 값 설정)
smote = SMOTE(random_state=42, k_neighbors=1)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# 7. GridSearchCV를 사용하여 Random Forest의 최적의 하이퍼파라미터 탐색
param_grid = {
    'n_estimators': [100, 200, 300],  # 줄여서 실행 시간 단축
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train_resampled, y_train_resampled)

# 8. 최적의 모델로 예측
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# 9. 성능 평가
unique_labels = y_test.unique()

# classification_report에서 labels와 target_names를 정확하게 매칭
print(classification_report(y_test, y_pred, labels=unique_labels, target_names=le_disease.inverse_transform(unique_labels), zero_division=1))
