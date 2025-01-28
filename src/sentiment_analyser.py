import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from collections import Counter
import matplotlib.pyplot as plt
import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
device = 0 if torch.cuda.is_available() else -1

def analyze_sentiment(text):
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    sentiment_analyzer = pipeline('sentiment-analysis',
                                  model=model,
                                  tokenizer=tokenizer,
                                  device=device)

    res = sentiment_analyzer(text)
    labels = [res['label'] for res in res]
    labels_counts = Counter(labels)
    print(res)

    plt.pie(labels_counts.values(), labels=labels_counts.keys(), autopct='%1.0f%%', startangle=140)
    plt.title('Distribuzione dei sentimenti', fontsize=20)
    plt.show()