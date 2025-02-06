const loginDiv = document.getElementById("login");
        const chatDiv = document.getElementById("chat");
        const nomeInput = document.getElementById("nome");
        const confirmarNomeBtn = document.getElementById("confirmarNome");
        const mensagensDiv = document.getElementById("mensagens");
        const mensagemInput = document.getElementById("mensagem");
        const enviarBtn = document.getElementById("enviar");
        let nome = "";

        // CONEXAO WS
        const websocket = new WebSocket("ws://localhost:8765");

        // EVENTO PARA NOME DO USUARIO E INICIO NO CHAT
        confirmarNomeBtn.addEventListener("click", () => {
            nome = nomeInput.value.trim();
            if (nome) {
                websocket.send(nome);
                loginDiv.style.display = "none";
                chatDiv.style.display = "flex";
            }
        });

        // MSG RECEBIDA
        websocket.onmessage = (event) => {
            const mensagem = event.data;
            const mensagemElement = document.createElement("div");

            // ESTILO PARA MSG
            if (mensagem.includes("[Sistema]")) {
                mensagemElement.className = "mensagem sistema";
            } else if (mensagem.includes(`[${nome}]`)) {
                mensagemElement.className = "mensagem minha";
            } else {
                mensagemElement.className = "mensagem usuario"; 
            }

            mensagemElement.textContent = mensagem;
            mensagensDiv.appendChild(mensagemElement);
            mensagensDiv.scrollTop = mensagensDiv.scrollHeight; // SCROLL
        };

        const enviarMensagem = () => {
            const mensagem = mensagemInput.value.trim();
            if (mensagem) {
                websocket.send(mensagem);
                mensagemInput.value = ""; 
            }
        };

        // EVENTOS P ENVIAR MSG
        enviarBtn.addEventListener("click", enviarMensagem);

        mensagemInput.addEventListener("keypress", (event) => {
            if (event.key === "Enter") {
                enviarMensagem();
            }
        });