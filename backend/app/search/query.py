# search logic
from sklearn.metrics.pairwise import cosine_similarity

def search(query, vectorizer, tfidf_matrix, documents, top_k=5):
    query_vec = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    related_docs_indices = cosine_similarities.argsort()[:-top_k-1:-1]
    
    results = []
    for idx in related_docs_indices:
        results.append({
            "url": documents[idx]['url'],
            "content": documents[idx]['content'],
            "score": cosine_similarities[idx]
        })
    
    return results  