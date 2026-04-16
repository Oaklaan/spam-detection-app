from flask import Flask, request, render_template

app = Flask(__name__)

def check_spam(text):
    spam_words = ["free", "win", "lottery", "prize"]
    return any(word in text.lower() for word in spam_words)

@app.route("/", methods=["GET", "POST"])   # ✅ FIX HERE
def home():
    result = ""
    
    if request.method == "POST":
        message = request.form.get("message")   # safer
        if message:
            if check_spam(message):
                result = "🚨 This message is SPAM!"
            else:
                result = "✅ This message is NOT Spam!"

    return render_template("index.html", result=result)

app.run(debug=True)