from nltk.tokenize import word_tokenize
from nltk import pos_tag

def analyse(keywords, topic):
    tokens_keywords = word_tokenize(keywords)
    tagged_keywords = pos_tag(tokens_keywords)
    tokens_topic = word_tokenize(topic)
    tagged_topic = pos_tag(tokens_topic)

    print("Tokens keyword:")
    for word, tag in tagged_keywords:
        print(f"({word}, {tag})")

    print("\nTagged Topic:")
    for word, tag in tagged_topic:
        print(f"({word}, {tag})")