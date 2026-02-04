console.log("JS LOADED");

async function sendMessage() {
    const input = document.getElementById("messageInput");
    const messages = document.getElementById("messages");

    const text = input.value.trim();
    if (!text) return;

    const userDiv = document.createElement("div");
    userDiv.className = "message user";
    userDiv.innerHTML = `
        <div class="bubble">${text}</div>
        <div class="emoji">🧑</div>
    `;
    messages.appendChild(userDiv);

    input.value = "";
    messages.scrollTop = messages.scrollHeight;

    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    });

    const data = await res.json();

    
    const botDiv = document.createElement("div");
    botDiv.className = "message bot";
    botDiv.innerHTML = `
        <div class="emoji">🤖</div>
        <div class="bubble">${data.reply}</div>
    `;
    messages.appendChild(botDiv);

    messages.scrollTop = messages.scrollHeight;
}
