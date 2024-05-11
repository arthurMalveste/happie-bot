import requests
import json

# Substitua por sua chave de API real
CHAVE_API = "AIzaSyDiUvSpASqqkBm-nwD5O-KWKbLSdxwM1wQ"

# Substitua pelo caminho do seu arquivo de áudio
CAMINHO_DO_ARQUIVO = "/static/audio/Record (online-voice-recorder.com).mp3"

# Configure os cabeçalhos da requisição
cabecalhos = {
    "Authorization": f"Bearer {CHAVE_API}",
    "Content-Type": "audio/wav",
}

# Leia o arquivo de áudio como dados binários
with open(CAMINHO_DO_ARQUIVO, "rb") as arquivo_de_audio:
    dados_de_audio = arquivo_de_audio.read()

# Envie a requisição POST para a API Gemini
resposta = requests.post(
    "https://api.gemini.ai/v1/transcribe",
    headers=cabecalhos,
    data=dados_de_audio,
)

# Verifique o status da resposta
if resposta.status_code == 200:
    # Analise a resposta JSON
    dados_da_resposta = json.loads(resposta.content)

    # Extraia o texto transcrito
    texto_transcrito = dados_da_resposta["texto"]

    # Imprima o texto transcrito
    print("Texto Transcrito:", texto_transcrito)
else:
    print("Erro ao transcrever o áudio:", resposta.status_code, resposta.text)