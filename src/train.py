import pandas as pd
import preprocessor as pp
import extractor_kw as kw
import ngram as ng
import showing_details as sd
import comparator as cmp

df = pd.read_csv('../dataset/dataset.csv', sep=';')

print("\nStep 1: Finding keywords (based on article text)\n")
print("Preprocessing text")
for i in range(df['text'].count()):
    preprocessing = pp.preprocess_text(df['text'][i])
    print(preprocessing)

print("\nExtraction keywords")
keywordsTextTable = []
for i in range(df['text'].count()):
    extractKeyWordsArticleText = kw.extract_kw(df['text'][i])
    keywordsTextTable.append(extractKeyWordsArticleText)
print(keywordsTextTable)

print("\nGenerating n-grams")
for i in range(df['text'].count()):
    answer = ng.generate_n_grams(df['text'][i])
    print("Sentence after removing stopwords = {}".format(answer))

keywordsText = ""
for i in range(len(keywordsTextTable)):
    for j in range(len(keywordsTextTable[i])):
        keywordsText = keywordsText + " " + keywordsTextTable[i][j]
        print(keywordsText)

answer = sd.generate_wordcloud(keywordsText)

print("\nStep 2: Topic analysis (based on article title)\n")
print("Preprocessing text")
for i in range(df['article'].count()):
    preprocessing = pp.preprocess_text(df['article'][i])
    print(preprocessing)

print("\nExtraction keywords")
keywordsTitleTable = []
for i in range(df['article'].count()):
    extractKeyWordsArticleTitle = kw.extract_kw(df['article'][i])
    keywordsTitleTable.append(extractKeyWordsArticleTitle)

print(keywordsTitleTable)

print("\nGenerating n-grams")
for i in range(df['article'].count()):
    answer = ng.generate_n_grams(df['article'][i])
    print("Sentence after removing stopwords = {}".format(answer))

keywordsTitle = ""
for i in range(len(keywordsTitleTable)):
    for j in range(len(keywordsTitleTable[i])):
        keywordsTitle = keywordsTitle + " " + keywordsTitleTable[i][j]

answer = sd.generate_wordcloud(keywordsTitle)

print("\nComparing keywords and article text")