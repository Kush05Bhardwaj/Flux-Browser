# builds TF-IDF
import json
from sklearn.feature_extraction.text import TfidfVectorizer

def build_index():
    with open('app/data/documents.json', 'r', encoding='utf-8') as f:
        documents = json.load(f)

    corpus = [doc['content'] for doc in documents]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    return {
        "vectorizer": vectorizer,
        "tfidf_matrix": tfidf_matrix,
        "documents": documents
    }