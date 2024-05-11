const loader = document.querySelector(".loader")
const divLoader = document.querySelector(".div-loader")
const inputChat = document.querySelector(".input-chat")
const sendBtn = document.querySelector(".btn-chat")
window.addEventListener('load', () => {
    divLoader.style.opacity = 0
    setTimeout(function(){
        divLoader.remove()
    }, 301)
})

function btnEnviar(){
    if (inputChat.value.length >= 1){
        sendBtn.classList.add("mostrar")
    } else{
        sendBtn.classList.remove("mostrar")
    }
}

function updateConversation(message) {
    const conversation = document.getElementById("conversation");
    conversation.innerHTML += `<p>${message}</p>`;
}