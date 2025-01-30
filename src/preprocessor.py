from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#This function preprocesses the text given in input
def preprocess_text(text):
    stop_words = set(stopwords.words('italian'))
    lemmatizer = WordNetLemmatizer()

    #Split the text into tokens
    tokens = word_tokenize(text)

    #Removing stop words and tokenizing them
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]

    return cleaned_tokens