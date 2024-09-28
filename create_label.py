import nltk # type: ignore
import re
from nltk.corpus import stopwords # type: ignore
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory # type: ignore
import joblib # type: ignore

# Download necessary NLTK data
nltk.download("punkt", quiet=True)  # Added quiet=True to suppress output
nltk.download("stopwords", quiet=True)

def get_label(news_text):
    # Convert to lowercase and tokenize
    lower = news_text.lower()
    tokens = nltk.word_tokenize(lower)  # Tokenize using NLTK

    # Remove punctuation and digits
    tokens = [re.sub(r'[.,()&=%:-]', '', token) for token in tokens]
    tokens = [re.sub(r'\d+', '', token) for token in tokens]

    # Filter out stop words
    stop_words = set(stopwords.words("indonesian"))
    filtered_tokens = [token for token in tokens if token and token not in stop_words]

    # Join tokens back into a single string
    filtered_text = " ".join(filtered_tokens)

    # Initialize stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stemmed_text = stemmer.stem(filtered_text)

    # Load the trained model and vectorizer
    vectorizer = joblib.load('model/tfidf_vectorizer')
    model = joblib.load('model/nb_model')

    # Transform the new text to feature vectors
    x_new = vectorizer.transform([stemmed_text]).toarray()
    
    # Make prediction
    prediction = model.predict(x_new)
    result = prediction[0]

    return result
