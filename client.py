import asyncio
import websockets

async def enviar_mensagens(websocket):
    while True:
        mensagem = input("Digite uma mensagem: ")
        await websocket.send(mensagem)

async def receber_mensagens(websocket):
    async for mensagem in websocket:
        print(f"\nNova mensagem: {mensagem}")

async def chat_cliente():
    async with websockets.connect("ws://localhost:8765") as websocket:
        try:
            nome = input("Digite seu nome: ")
            await websocket.send(nome)
            print("Conectado ao servidor de chat!")

            await asyncio.gather(
                enviar_mensagens(websocket),
                receber_mensagens(websocket)
            )
        except websockets.exceptions.ConnectionClosedError:
            print("Conexão com o servidor perdida.")

asyncio.run(chat_cliente())