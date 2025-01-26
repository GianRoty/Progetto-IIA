import pandas as pd
import preprocessor as pp
import extractor_kw as kw
import ngram as ng
import showing_details as sd

df = pd.read_csv('../dataset/dataset.csv', sep=';')

print("Preprocessing text")

for i in range(df['text'].count()):
    preprocessing = pp.preprocess_text(df['text'][i])
    print(preprocessing)

print("\nExtraction keywords")

for i in range(df['text'].count()):
    extractKeyWords = kw.extract_kw(df['text'][i])
    print(extractKeyWords)

print("\nGenerating n-grams")

for i in range(df['text'].count()):
    answer = ng.generate_n_grams(df['text'][i])
    print("Sentence after removing stopwords = {}".format(answer))

for i in range(df['text'].count()):
    answer = sd.generate_wordcloud(df['text'][i])