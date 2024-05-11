from flask import Flask, request

app = Flask(__name__)

# Configuration (replace with your actual values)
GEMINI_API_KEY = 'AIzaSyDiUvSpASqqkBm-nwD5O-KWKbLSdxwM1wQ'  # Your Gemini API key

def transcribe_audio(audio_file):
    import requests
    import json

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "audio/mp3",
    }

    response = requests.post(
        "https://api.gemini.ai/v1/transcribe",
        headers=headers,
        files={'audio_file': audio_file}
    )

    if response.status_code == 200:
        data = json.loads(response.content)
        return data.get("texto")  # Extract the transcribed text
    else:
        print("Error transcribing audio:", response.status_code, response.text)
        return None

@app.route('/')
def principal():
    
    return app.send_static_file('teste.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_file = request.files['audio_file']
    transcription = transcribe_audio(audio_file)
    return transcription
    



if __name__ == '__main__':
    app.run(debug=True)
