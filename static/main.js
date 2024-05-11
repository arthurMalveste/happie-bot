function updateConversation(message) {
    const conversation = document.getElementById("conversation");
    conversation.innerHTML += `<p>${message}</p>`;
}