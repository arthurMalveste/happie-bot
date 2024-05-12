const loader = document.querySelector(".loader")
const divLoader = document.querySelector(".div-loader")
const inputChat = document.querySelector(".input-chat")
const sendBtn = document.querySelector(".btn-chat")
const happie = document.querySelector(".icon-happie")
const nameHappie = document.querySelector(".name-happie")
const logo = document.querySelectorAll(".name-happie path")

window.addEventListener('load', () => {
    if (!localStorage.getItem('loadStat')){
        loader.style.opacity = 0
        setTimeout(function(){
            loader.remove()
            happie.style.opacity = 1
            setTimeout(function(){
                happie.style.transform = "translate(-120%, -50%)"
                nameHappie.style.opacity = 1
                nameHappie.style.transform = "translate(-7.5%, -50%)"
                logo.forEach(element => {
                    element.classList.add("animarHappie")
                })
                setTimeout(function() {
                    nameHappie.classList.add("fillHappie")
                    setTimeout(function(){
                        divLoader.style.opacity = 0
                        setTimeout(function(){
                            divLoader.remove()
                            localStorage.setItem('loadStat', true)
                        }, 300)
                    }, 800)
                }, 1500)
            }, 500)
        }, 300)
    } else if (localStorage.getItem('loadStat')){
        divLoader.style.opacity = 0
        setTimeout(function(){
            divLoader.remove()
        }, 300)
    } else{
        console.error();
    }
})

inputChat.addEventListener('input', () => {
    if (inputChat.value.length >= 1){
        sendBtn.classList.add("mostrar")
    } else{
        sendBtn.classList.remove("mostrar")
    }
})

function updateConversation(message) {
    const conversation = document.getElementById("conversation");
    conversation.innerHTML += `<p>${message}</p>`;
}