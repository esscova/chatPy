import asyncio
import websockets

conexoes = set()

async def chat(websocket):
    conexoes.add(websocket)
    print(f"Novo cliente conectado! Total de clientes: {len(conexoes)}")

    try:
        async for mensagem in websocket:
            print(f"Mensagem recebida: {mensagem}")
            for conexao in conexoes:
                if conexao != websocket:  
                    await conexao.send(f"Cliente diz: {mensagem}")
    finally:
        conexoes.remove(websocket)
        print(f"Cliente desconectado. Total de clientes: {len(conexoes)}")

async def main():
    async with websockets.serve(chat, "localhost", 8765):
        print("Servidor de chat WebSocket iniciado em ws://localhost:8765")
        await asyncio.Future()  

asyncio.run(main())