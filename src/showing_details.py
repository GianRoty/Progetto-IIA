import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_wordcloud(text):
    wordcloud = WordCloud(width = 500, height = 500, background_color = "white").generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    return wordcloud