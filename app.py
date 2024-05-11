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

# Lista de saudações amigáveis
saudacoes = ["Oi!", "Olá!", "E aí?", "Oi! Como você está?", "Oi, amigo!"]

# Lista de despedidas amigáveis
despedidas = ["Até mais!", "Até logo!", "Tchau! Volte logo!", "Até mais tarde, amigo!"]

# Lista de emojis amigáveis
emojis = [":)", ":D", ";)", ":P", "<3"]

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/salvar_dados", methods=["POST"])
def salvar_dados():
    # Obter os dados do formulário enviado pelo método POST
    nome = request.form["nome"]
    idade = request.form["idade"]

    # Salvar os dados nas variáveis respectivas
    # Aqui você pode fazer o que quiser com os dados, como salvá-los em um banco de dados ou usá-los em outra parte do código

    # Exemplo de uso: salvar em variáveis globais
    global nome_salvo
    global idade_salva
    nome_salvo = nome
    idade_salva = idade


    # Redirecionar para outra página ou retornar uma mensagem de sucesso
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_response():
    user_message = request.form["message"]
    
    # Adicionar um prefixo ao prompt
    prefixed_message = "Faça uma mensagem bonita e amigavel de um paragrafo só, responda a pergunta mais haja como se fosse meu amigo, dependendo da idade converce como se fosse da idade também, se for uma pessoa com 35 anos ou mais não opte por gírias e nem assuntos mais infantis, se a idade for extremamente grande pergunte como piada se esta idade é ralmente a deel. Olá meu nome é: " + nome_salvo + "e eu tenho:" + idade_salva + "responda essa pergunta:" + user_message

    # Verificar se a mensagem do usuário é uma saudação
    if user_message.lower() in ["oi", "olá", "e aí", "olá amigo", "olá amiga"]:
        greeting = random.choice(saudacoes)
        response = chat.send_message(greeting)
        conversation = [greeting] + response.text.split('\n')
    else:
        # Responder de forma amigável
        response = chat.send_message(prefixed_message)
        conversation = [user_message] + response.text.split('\n')

    if idade_salva < "30":
    # Adicionar emoji aleatório
        emoji = random.choice(emojis)
        conversation[-1] += " " + emoji


    return render_template("index.html", conversation=conversation)

@app.route("/bye")
def bye():
    # Adicionar despedida aleatória
    goodbye = random.choice(despedidas)
    return goodbye

if __name__ == "__main__":
    app.run(debug=True, host=('0.0.0.0'))