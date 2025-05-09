from flask import Flask, render_template, request, jsonify, session
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load FAQ data
faq_data = pd.read_csv('faq_data.csv')

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
vectorized_questions = tfidf_vectorizer.fit_transform(faq_data['Question'])

# Chatbot response function
def chatbot_response(user_query):
    user_vector = tfidf_vectorizer.transform([user_query])
    similarities = cosine_similarity(user_vector, vectorized_questions).flatten()
    max_similarity_index = similarities.argmax()

    if similarities[max_similarity_index] > 0.3:
        response = faq_data.iloc[max_similarity_index]['Response']
    else:
        response = "I'm sorry, I couldn't understand your query. Please contact us at support@spongeco.com."
    return response

# Sentiment Analysis
def analyze_sentiment(user_query):
    analysis = TextBlob(user_query)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_query = request.form.get('message')
        response = chatbot_response(user_query)
        sentiment = analyze_sentiment(user_query)
        return jsonify({"response": response, "sentiment": sentiment})
    return render_template('chat.html')

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart_items=cart_items)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = request.json.get('item')
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(item)
    session.modified = True
    return jsonify({"message": "Item added to cart"})

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    item = request.json.get('item')
    if 'cart' in session and item in session['cart']:
        session['cart'].remove(item)
        session.modified = True
    return jsonify({"message": "Item removed from cart"})

if __name__ == "__main__":
    app.run(debug=True)
