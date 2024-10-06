import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# 1. 데이터 불러오기
df1 = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\중복제거_데이터1.csv", encoding='utf-8')

# 2. 필요한 컬럼 추출 (성분명A, 성분코드A, 성분명B, 성분코드B, 상세_비고_병합(부작용))
df_column1 = df1[['성분명A', '성분코드A', '성분명B', '성분코드B', '상세_비고_병합']]

# 3. Label Encoding (범주형 데이터를 숫자로 변환)
le = LabelEncoder()
df_column1['성분명A'] = le.fit_transform(df_column1['성분명A'])
df_column1['성분코드A'] = le.fit_transform(df_column1['성분코드A'])
df_column1['성분명B'] = le.fit_transform(df_column1['성분명B'])
df_column1['성분코드B'] = le.fit_transform(df_column1['성분코드B'])
df_column1['상세_비고_병합'] = le.fit_transform(df_column1['상세_비고_병합'])

# 4. 학습용 데이터와 레이블 분리
X = df_column1[['성분명A', '성분코드A', '성분명B', '성분코드B']]
y = df_column1['상세_비고_병합']

# 5. y 값 재정렬 (누락된 값 처리)
_, y_reindexed = np.unique(y, return_inverse=True)

# 6. 학습 데이터와 테스트 데이터 분리 (80% 학습, 20% 테스트)
X_train, X_test, y_train, y_test = train_test_split(X, y_reindexed, test_size=0.2, random_state=42)

# 7. XGBoost 모델 생성 및 학습
model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X_train, y_train)

# 8. 예측
y_pred = model.predict(X_test)

# 9. 정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print(f"모델 정확도: {accuracy * 100:.2f}%")
