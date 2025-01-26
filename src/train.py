import pandas as pd
import preprocessor as pp
import extractor_kw as kw
import ngram as ng

df = pd.read_csv('../dataset/dataset.csv', sep=';')

print("=========================================================")
print("Preprocessing text")
print("=========================================================")

for i in range(df['text'].count()):
    preprocessing = pp.preprocess_text(df['text'][i])
    print(preprocessing)

print("=========================================================")
print("Extraction keywords")
print("=========================================================")

for i in range(df['text'].count()):
    extractKeyWords = kw.extract_kw(df['text'][i])
    print(extractKeyWords)

print("==========================================================")
print("Stemming/Lemmatization as well as n-grams")
print("==========================================================")
for i in range(df['text'].count()):
    answer = ng.generate_n_grams(df['text'][i])
    print("Sentence after removing stopwords = {}".format(answer))
    print("==========================================================")