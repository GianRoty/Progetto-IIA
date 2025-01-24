from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#Preprocessa il testo passato come parametro
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    #Tokenizzazione
    tokens = word_tokenize(text)

    #Rimozione stop words e tokenizzazione
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]

    return cleaned_tokens