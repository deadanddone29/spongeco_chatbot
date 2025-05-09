SpongeCo Application
SpongeCo is a simple e-commerce web application for selling sponges, featuring a chatbot for customer service and a cart functionality for managing products.

Features

Homepage: Displays a catalog of products with "Add to Cart" buttons.
Cart: Allows users to view and manage items added to their cart.
Chatbot: Provides customer support with FAQ-based responses and sentiment analysis.
Navigation: Includes a fixed navigation bar for easy access to the cart and chatbot.

Tech Stack

Backend:
Flask: Python web framework for backend logic and routing.
Pandas: For managing chatbot FAQ data.
scikit-learn: For vectorization and similarity calculations.
TextBlob: For sentiment analysis.

Frontend:
HTML/CSS: For static templates and styling.
JavaScript (Fetch API): For dynamic interactions like adding to cart and chatbot responses.

Getting Started

pip install flask pandas scikit-learn textblob
Start the Flask development server:
python app.py
http://127.0.0.1:5000

SpongeCo Application
├── app.py             
├── static/
│   ├── images/        
│   ├── css/           
├── templates/
│   ├── index.html     
│   ├── chat.html      
│   ├── cart.html     
├── faq_data.csv      
├── README.md         
└── requirements.txt   

Features Overview
1. Homepage
Displays a grid of products with names, descriptions, and "Add to Cart" buttons.
Navigation bar at the top for easy access to cart and chatbot.
2. Cart
Displays the items added to the cart.
Allows users to remove items dynamically.
3. Chatbot
Answers user queries based on FAQ data (faq_data.csv).
Analyzes the sentiment of user messages and provides appropriate feedback

API Endpoints
Routes:
/: Displays the homepage.
/chat: Displays the chatbot page and handles chat queries.
/cart: Displays the cart page with added items.
/add_to_cart: Handles adding items to the cart (POST).
/remove_from_cart: Handles removing items from the cart (POST).