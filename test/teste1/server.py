from flask import Flask, render_template, request
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import os
import requests
import json

app = Flask(__name__)

# Configurações
GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY'  # Sua chave de API do Gemini

# Função para transcrever áudio usando a API do Gemini
def transcrever_audio(audio_file):
    url = 'https://api.gemini.ai/v1/transcribe'
    headers = {
        'Authorization': f'Bearer {GEMINI_API_KEY}'
    }
    files = {
        'audio_file': audio_file
    }
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data.get('texto')
    else:
        return f"Erro ao transcrever áudio: {response.status_code} - {response.text}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gravar', methods=['POST'])
def gravar():
    fs = 44100  # Taxa de amostragem
    duration = 5  # Duração da gravação em segundos
    recording = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Aguarda a gravação ser concluída

    # Salva a gravação em um arquivo WAV
    wavfile.write('audio.wav', fs, recording)

    with open('audio.wav', 'rb') as f:
        audio_data = f.read()

    # Exclui o arquivo WAV
    os.remove('audio.wav')

    # Transcrever o áudio
    texto_transcrito = transcrever_audio(('audio_file', audio_data))

    return texto_transcrito

if __name__ == '__main__':
    app.run(debug=True)
