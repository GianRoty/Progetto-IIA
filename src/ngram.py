from nltk.corpus import stopwords

def generate_n_grams(text, ngram = 3):
    words = [word for word in text.split(" ") if word not in set(stopwords.words('italian'))]
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans = [' '.join(ngram) for ngram in temp]
    return ans