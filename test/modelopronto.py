import google.generativeai as genai

import os
print(f"Diretório atual: {os.getcwd()}")

# Substitua 'YOUR_API_KEY' pela sua chave de API do Gemini
genai.configure(api_key='AIzaSyDiUvSpASqqkBm-nwD5O-KWKbLSdxwM1wQ')

# Defina o caminho para o seu arquivo de áudio
audio_file_path = "E:/gemini ai/test"

# Leia o arquivo de áudio como bytes
with open(audio_file_path, 'rb') as f:
    audio_file_bytes = f.read()

# Carregue os bytes do arquivo de áudio para o Gemini File API
audio_file = genai.upload_file(audio_file_path)

# Defina o prompt de texto
prompt = """
Listen carefully to the audio file. Provide transcription with maximum accuracy
Try to identify who the speaker is...
"""

# Crie um modelo Gemini
model = genai.GenerativeModel(model='models/gemini-1.5-pro-latest')

# Gere o conteúdo usando o prompt de texto e o arquivo de áudio
response = model.generate_content([prompt, audio_file])

# Imprima a resposta
print(response.text)