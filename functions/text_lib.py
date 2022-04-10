import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('omw-1.4')

def preprocessing(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stopWords = set(stopwords.words('portuguese'))
    words = [WordNetLemmatizer().lemmatize(w) for w in tokens if (w and w not in stopWords)]
    return words