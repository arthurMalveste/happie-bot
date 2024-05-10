from config import *

# Desenvolvimeto do app

chat = model.start_chat(history=[])

prompt = input('Esperando prompt: ')

while prompt != "fim":
  response = chat.send_message(prompt)
  print("Resposta:", response.text, '\n\n')
  prompt = input('Esperando prompt: ')



