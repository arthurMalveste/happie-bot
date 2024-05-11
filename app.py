from config import *
from flask import Flask, render_template, request
from apikey import *
import random
from list import *


app = Flask(__name__)

# Configuração do modelo
model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Inicialização do chat
chat = model.start_chat(history=[])

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
    prefixed_message = "Faça uma mensagem bonita e amigavel de um paragrafo só, responda a pergunta mais haja como se fosse meu amigo, dependendo da idade converce como se fosse da idade também, se for uma pessoa com 35 anos ou mais não opte por gírias e nem assuntos mais infantis, se a idade for extremamente grande pergunte como piada se esta idade é ralmente a dele. Olá meu nome é: " + nome_salvo + " e eu tenho: " + idade_salva + " responda essa pergunta: " + user_message

    response = chat.send_message(prefixed_message)

    # Combine response lines into a single string
    ai_response = response.text.replace('\n', ' ')
     # Substitui quebras de linha por espaços

    conversation = []
    conversation.append(user_message)
    conversation.append(ai_response) # Adiciona a resposta completa do Gemini

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

@app.route("/pergunta_aleatoria")
def pergunta_aleatoria():
    pergunta = random.choice(perguntas)

@app.route("/frases_motivacionais")
def frases_motivacionais():
    frases = random.choice(frases_motivacionais)

@app.route("/elogios")
def elogios():
    elogio = random.choice(elogios)

@app.route("/curiosidades")
def pergunta_aleatoria():
    curiosidade = random.choice(curiosidades)



if __name__ == "__main__":
    app.run(debug=True, host=('0.0.0.0'))