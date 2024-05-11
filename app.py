from config import *
from flask import Flask, render_template, request
from apikey import *
import random


app = Flask(__name__)

# Configuração do modelo
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings)
# Inicialização do chat
chat = model.start_chat(history=[])


saudacoes = ["Oi!", "Olá!", "E aí?", "Oi! Como você está?", "Oi, amigo!"]

despedidas = ["Até mais!", "Até logo!", "Tchau! Volte logo!", "Até mais tarde, amigo!"]

emojis = [":)", ":D", ";)", ":P", "<3"]

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/salvar_dados", methods=["POST"])
def salvar_dados():
    # Obter os dados do formulário enviado pelo método POST
    nome = request.form["nome"]
    idade = request.form["idade"]


    # Exemplo de uso: salvar em variáveis globais
    global nome_salvo
    global idade_salva
    nome_salvo = nome
    idade_salva = idade

    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_response():
    # Retrieve user message from POST data
    user_message = request.form["message"]

    # Add prefix to the prompt
    prefixed_message = "Faça uma mensagem bonita e amigavel de um paragrafo só, responda a pergunta mais haja como se fosse meu amigo, dependendo da idade converce como se fosse da idade também, se for uma pessoa com 35 anos ou mais não opte por gírias e nem assuntos mais infantis, se a idade for extremamente grande pergunte como piada se esta idade é ralmente a dele. Olá meu nome é: " + nome_salvo + "e eu tenho:" + idade_salva + "responda essa pergunta:" + user_message

    response = chat.send_message(prefixed_message)

    conversation = []

    conversation.append(user_message)

    response_lines = response.text.split('\n')

    # Add chatbot response lines to the conversation list
    conversation.extend(response_lines)

    if idade_salva < "30":
        # Add emoji randomly
        emoji = random.choice(emojis)
        conversation[-1] += " " + emoji

    # Return the conversation list
    return render_template("index.html", conversation=conversation)


@app.route("/bye")
def bye():
    # Adicionar despedida aleatória
    goodbye = random.choice(despedidas)
    return goodbye

# @app.route("/pular")
# def pular():
    
#     return ("/")

if __name__ == "__main__":
    app.run(debug=True, host=('0.0.0.0'))