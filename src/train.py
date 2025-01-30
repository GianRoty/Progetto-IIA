import pandas as pd
import preprocessor as pp
import extractor_kw as kw
import ngram as ng
import showing_details as sd
import comparator as cmp
import lexer as lex
import sentiment_analyzer as sa

df = pd.read_csv('../dataset/prison_corpus.tsv', sep='\t', header=0)

print("\nTask 1: Finding keywords (based on article text)\n")
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
    ngramResult = ng.generate_n_grams(df['text'][i])
    print("Sentence after removing stopwords = {}".format(ngramResult))

keywordsText = ""
for i in range(len(keywordsTextTable)):
    for j in range(len(keywordsTextTable[i])):
        keywordsText = keywordsText + " " + keywordsTextTable[i][j]

answer = sd.generate_wordcloud(keywordsText)

print("\nTask 2: Topic analysis (based on article title)\n")
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
    ngramResult = ng.generate_n_grams(df['article'][i])

keywordsTitle = ""
for i in range(len(keywordsTitleTable)):
    for j in range(len(keywordsTitleTable[i])):
        keywordsTitle = keywordsTitle + " " + keywordsTitleTable[i][j]

answer = sd.generate_wordcloud(keywordsTitle)

print("\nComparing keywords and article text")
result = cmp.compare(keywordsTitle, keywordsText)
print(result)

print("\nTask 3: Lexical analysis")
lex.analyse(keywordsTitle, keywordsText)

print("\nTask 4: Sentiment analysis")
sa.analyze_sentiment(keywordsText)
