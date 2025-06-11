
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample FAQ data
faq_data = {
    "order": "To place an order, browse restaurants, add items to cart, and checkout.",
    "cancel": "Go to 'My Orders' and cancel before the food is prepared.",
    "delivery": "Standard delivery takes 30–45 minutes.",
    "payment": "We accept UPI, credit/debit cards, and wallets.",
    "track": "Track your order in 'My Orders' section.",
    "promo": "Apply promo codes during checkout.",
    "address": "Update delivery address under your profile settings.",
    "support": "Contact support from the Help section in the app.",
    "refund": "Refunds take 5–7 business days after cancellation."
}

def find_answer(question):
    question = question.lower()
    for keyword in faq_data:
        if keyword in question:
            return faq_data[keyword]
    return "Sorry, I couldn’t find the answer. Please contact support."

@app.route('/')
def home():
    return render_template('foodappui.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        question = request.form.get('question', '')
        print("User asked:", question)
        answer = find_answer(question)
        return jsonify({'response': answer})
    except Exception as e:
        print("Error:", e)
        return jsonify({'response': "Oops! Something went wrong on the server."})

if __name__ == '__main__':
    app.run(debug=True)
