const loginDiv = document.getElementById("login");
        const chatDiv = document.getElementById("chat");
        const nomeInput = document.getElementById("nome");
        const confirmarNomeBtn = document.getElementById("confirmarNome");
        const mensagensDiv = document.getElementById("mensagens");
        const mensagemInput = document.getElementById("mensagem");
        const enviarBtn = document.getElementById("enviar");
        let nome = "";

        const websocket = new WebSocket("ws://localhost:8765");

        confirmarNomeBtn.addEventListener("click", () => {
            nome = nomeInput.value.trim();
            if (nome) {
                websocket.send(nome);
                loginDiv.style.display = "none";
                chatDiv.style.display = "flex";
            }
        });

        websocket.onmessage = (event) => {
            const mensagem = event.data;
            const mensagemElement = document.createElement("div");
            let classes = "px-4 py-2 rounded-lg max-w-md";

            if (mensagem.includes("[Sistema]")) {
                classes += " bg-gray-100 text-gray-700";
                mensagemElement.className = classes;
            } else if (mensagem.includes(`[${nome}]`)) {
                classes += " bg-blue-600 text-white ml-auto";
                mensagemElement.className = classes;
            } else {
                classes += " bg-gray-200 text-gray-800";
                mensagemElement.className = classes;
            }

            mensagemElement.textContent = mensagem;
            mensagensDiv.appendChild(mensagemElement);
            mensagensDiv.scrollTop = mensagensDiv.scrollHeight;
        };

        const enviarMensagem = () => {
            const mensagem = mensagemInput.value.trim();
            if (mensagem) {
                websocket.send(mensagem);
                mensagemInput.value = "";
            }
        };

        enviarBtn.addEventListener("click", enviarMensagem);

        mensagemInput.addEventListener("keypress", (event) => {
            if (event.key === "Enter") {
                enviarMensagem();
            }
        });