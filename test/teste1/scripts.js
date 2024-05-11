const recordButton = document.getElementById('recordButton');
const stopButton = document.getElementById('stopButton');
const translationDiv = document.getElementById('translation');

let mediaRecorder;
let audioChunks = [];

recordButton.addEventListener('click', () => {
  startRecording();
});

stopButton.addEventListener('click', () => {
  stopRecording();
});

function startRecording() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      mediaRecorder = new MediaRecorder(stream);
      mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
      };
      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        translateAudio(audioBlob);
      };
      mediaRecorder.start();
      recordButton.disabled = true;
      stopButton.disabled = false;
    })
    .catch(err => {
      console.error('Erro ao acessar o microfone:', err);
    });
}

function stopRecording() {
  mediaRecorder.stop();
  audioChunks = [];
  recordButton.disabled = false;
  stopButton.disabled = true;
}

function translateAudio(audioBlob) {
  const formData = new FormData();
  formData.append('audio', audioBlob, 'audio.wav');

  fetch('/translate', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    translationDiv.textContent = data.translation;
    processWithGemini(data.translation);
  })
  .catch(err => {
    console.error('Erro na tradução:', err);
  });
}

function processWithGemini(text) {
  // Substitua pela sua lógica para processar o texto com o Gemini
  console.log("Processando com Gemini:", text);
  // Exemplo: Envie o texto para o Gemini e exiba a resposta
  fetch('/process_with_gemini', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text: text }),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Resposta do Gemini:', data.response);
  })
  .catch(err => {
    console.error('Erro ao processar com Gemini:', err);
  });
}