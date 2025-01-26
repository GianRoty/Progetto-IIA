from nltk.corpus import stopwords

def generate_n_grams(text, ngram=1):
    words = [word for word in text.split(" ") if word not in set(stopwords.words('english'))]
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans = [' '.join(ngram) for ngram in temp]
    return ans