import google.generativeai as genai
import requests

# Substitua pela sua chave da API do Gemini
GOOGLE_API_KEY = "AIzaSyDiUvSpASqqkBm-nwD5O-KWKbLSdxwM1wQ"
genai.configure(api_key=GOOGLE_API_KEY)

URL = "https://www.zedge.net/find/ringtones/hello%20(wav)"

# Baixar o arquivo WAV com a biblioteca requests
response = requests.get(URL)
with open('hello.wav', 'wb') as f:
    f.write(response.content)

# Upload do arquivo para a API usando o caminho do arquivo
audio_file = genai.upload_file('hello.wav')

prompt = "Create a transcript of the audio file."
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
response = model.generate_content([prompt, audio_file])

# Imprime a transcrição sem formatação Markdown
print(response.text) 