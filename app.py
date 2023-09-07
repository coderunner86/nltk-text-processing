import nltk
import json
from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('words')
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

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

@app.route('/')
def best_match_audience():
    try:
        # Obtener la palabra y la lista de audiencias de la query string
        input_word = request.args.get('word', '')
        input_audiences = request.args.getlist('audiences')

        if not input_word or not input_audiences:
            return jsonify({"error": "Word and Audiences are required in query string"})

        # Procesar la palabra de entrada
        processed_word = preprocess_text(input_word)

        # Encontrar el mejor match en la lista de audiencias
        best_match = find_best_match(processed_word, input_audiences)

        return jsonify({"best_match": best_match})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5001, debug=False)
