import pandas as pd
import preprocessor as pp

df = pd.read_csv('../dataset/dataset.csv', sep=';')

for i in range(df['text'].count()):
    preprocessing = pp.preprocess_text(df['text'][i])
    print(preprocessing)