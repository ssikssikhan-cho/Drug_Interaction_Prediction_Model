import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

# 1. 데이터 로드
df = pd.read_csv("C:\\Users\\Eunsoo\\Desktop\\의약품안전사용서비스(DUR) 의약품 목록 2020~2023\\상세_비고_병합만 중복제거_데이터1.csv", encoding='utf-8')

# 2. Sentence-BERT 모델 로드 (SBERT)
model = SentenceTransformer('all-MiniLM-L6-v2')

# 3. "상세_비고_병합" 컬럼의 문장들을 리스트로 변환
sentences = df['상세_비고_병합'].tolist()

# 4. 문장 임베딩 벡터 생성
sentence_embeddings = model.encode(sentences)

print(f"임베딩 벡터 크기: {sentence_embeddings.shape}")

# 5. K-Means 클러스터링 수행
num_clusters = 200  # 클러스터 수를 설정 (원하는 수로 변경 가능)
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(sentence_embeddings)

# 각 텍스트의 클러스터 번호 할당 (이 데이터는 메모리에서만 유지)
df['cluster'] = kmeans.labels_

# 6. 각 클러스터의 대표 텍스트를 선택하는 함수 정의
def get_representative_text(cluster_num):
    indices = np.where(kmeans.labels_ == cluster_num)[0]
    cluster_embeddings = sentence_embeddings[indices]
    centroid = kmeans.cluster_centers_[cluster_num]
    distances = np.linalg.norm(cluster_embeddings - centroid, axis=1)
    return df.iloc[indices[np.argmin(distances)]]['상세_비고_병합']

# 7. 각 클러스터에서 대표 텍스트로 치환
df['상세_비고_병합_대표'] = df['cluster'].apply(get_representative_text)

# 8. DBSCAN 클러스터링 (선택 사항)
dbscan = DBSCAN(eps=0.5, min_samples=5, metric='cosine')
dbscan_labels = dbscan.fit_predict(sentence_embeddings)
df['dbscan_cluster'] = dbscan_labels

# 9. 클러스터 결과 확인
for cluster_num in range(num_clusters):
    cluster_texts = df[df['cluster'] == cluster_num]['상세_비고_병합'].tolist()
    print(f"클러스터 {cluster_num}의 예시 텍스트: {cluster_texts[:3]}")

# 10. 결과를 새로운 파일로 저장 (기존 파일은 수정하지 않음)
df.to_csv('자연어처리된 상세_비고_병합1.csv',index=False, encoding='utf-8-sig')

# 데이터 확인
print(df[['상세_비고_병합', '상세_비고_병합_대표', 'cluster']].head())


