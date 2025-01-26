import pandas as pd
import preprocessor as pp
import extractor_kw as kw

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