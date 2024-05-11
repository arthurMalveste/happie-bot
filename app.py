from config import *
from flask import Flask, render_template, request
from apikey import *


app = Flask(__name__)

# Configuração do modelo
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Inicialização do chat
chat = model.start_chat(history=[])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_response():
    user_message = request.form["message"]
    response = chat.send_message(user_message)
    return render_template("index.html", conversation=[user_message, response.text])


if __name__ == "__main__":
    app.run(debug=True, host=('0.0.0.0'))
