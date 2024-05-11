const loader = document.querySelector(".loader")
const divLoader = document.querySelector(".div-loader")
window.addEventListener('load', () => {
    divLoader.style.opacity = 0
    setTimeout(function(){
        divLoader.remove()
    }, 301)
})

function updateConversation(message) {
    const conversation = document.getElementById("conversation");
    conversation.innerHTML += `<p>${message}</p>`;
}