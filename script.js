function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value;

    if (message.trim() === "") return;

    addMessage(message, "user");
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    })
    .then(res => res.json().catch(() => ({})).then(data => ({res, data})))
    .then(({res, data}) => {
        const reply = data && data.reply ? data.reply : `HTTP ${res.status} (no reply)`;
        addMessage(reply, "bot");
    })
    .catch(err => {
        console.error(err);
        addMessage("Request failed. Check console/network.", "bot");
    });
}


function addMessage(text, sender) {
    let chatBox = document.getElementById("chatBox");
    let msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}
