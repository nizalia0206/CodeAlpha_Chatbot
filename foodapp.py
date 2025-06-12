

from flask import Flask, render_template, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Simple FAQ database
faq = {
    "how to order": "To order, browse our menu, add items to your cart, and click checkout!",
    "cancel my order": "You can cancel your order within 5 minutes by going to 'My Orders' and selecting cancel.",
    "delivery time": "Delivery typically takes between 30 to 45 minutes.",
    "how can i pay": "You can pay via credit/debit cards, UPI, or cash on delivery.",
    "track my food": "Go to 'My Orders' and tap on 'Track Order' to see real-time updates.",
    "apply promo code": "You can apply promo codes during checkout before making payment.",
    "change delivery address": "To change your address, go to Profile > Addresses and update your info.",
    "contact support": "Reach us anytime via the Help section in the app or call our support line.",
    "refund": "Refunds are processed within 5-7 business days after cancellation."
}

def get_answer(question):
    question = question.lower()
    for key in faq:
        if key in question:
            return faq[key]
    return "Sorry, I couldn't understand that. Please try another question."

@app.route("/")
def index():
    questions = list(faq.keys())
    return render_template("foodappui.html", questions=questions)

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question", "")
    answer = get_answer(question)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
