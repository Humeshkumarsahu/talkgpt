from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API key set karo (apna key lagao)
genai.configure(api_key="AIzaSyCAwAeADpWhmK35XMuv9Qxshoua2zP1ZDM")

chat_history = []

@app.route("/")
def index():
    return render_template("index.html", chat=chat_history)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form["message"]
    chat_history.append({"role": "user", "content": user_msg})

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_msg)

    bot_reply = response.text
    chat_history.append({"role": "bot", "content": bot_reply})

    return render_template("index.html", chat=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
