from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compare(keywords, topic):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([" " + keywords, " " + topic])
    similarities = cosine_similarity(tfidf[0], tfidf[1])
    return similarities[0][0]