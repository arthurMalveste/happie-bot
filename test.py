import os
from config import *  # Assuming config.py stores GenAI API key etc.
from flask import Flask, render_template, request

app = Flask(__name__)

# Load your GenAI API key from a secure environment variable
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.9,
}

safety_settings = {
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL': 'BLOCK_NONE',
    'DANGEROUS': 'BLOCK_NONE'
}

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings)

chat = model.start_chat(history=[])


@app.route("/")
def index():
    return render_template("index.html", conversation=[])  # Initial empty conversation


@app.route("/chat", methods=["POST"])
def chat_response():
    user_message = request.form["message"]
    response = chat.send_message(user_message)
    conversation = [user_message, response.text]
    return render_template("index.html", conversation=conversation)


if __name__ == "__main__":
    app.run(debug=True)
