from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

app = Flask(__name__)

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

# Routes
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

if __name__ == "__main__":
    app.run(debug=True)
