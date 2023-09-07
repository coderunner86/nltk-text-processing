import nltk
import json
import random
from flask import Flask, request, jsonify

nltk.download('words')
nltk.download('punkt')

app = Flask(__name__)

english_words = set(nltk.corpus.words.words())

# Generate a random audience
@app.route('/')
def generate_random_audience():
    import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('words')
nltk.download('punkt')
nltk.download('stopwords')
def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [WordNetLemmatizer().lemmatize(word.lower()) for word in tokens if word.isalnum() and word.lower() not in stop_words]
    return ' '.join(tokens)

def calculate_similarity(input_str, target_str):
    input_set = set(input_str.split())
    target_set = set(target_str.split())
    intersection = len(input_set.intersection(target_set))
    union = len(input_set.union(target_set))
    similarity = intersection / union if union != 0 else 0.0
    return similarity

def find_best_match(processed_input, custom_audiences):
    best_match = 'None'
    max_similarity = 0

    for audience in custom_audiences:
        similarity = calculate_similarity(processed_input, preprocess_text(audience))
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = audience

    return best_match


if __name__ == '__main__':
    app.run(port=5001, debug=False)
