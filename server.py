import asyncio
import websockets

conexoes = set()

async def chat(websocket):
    conexoes.add(websocket)
    nome = await websocket.recv()  
    print(f"{nome} conectou-se! Total de clientes: {len(conexoes)}")

    try:
        async for mensagem in websocket:
            print(f"{nome} diz: {mensagem}")
            for conexao in conexoes:
                if conexao != websocket:
                    await conexao.send(f"{nome} diz: {mensagem}")
    finally:
        conexoes.remove(websocket)
        print(f"{nome} desconectou. Total de clientes: {len(conexoes)}")

async def main():
    async with websockets.serve(chat, "localhost", 8765):
        print("Servidor de chat WebSocket iniciado em ws://localhost:8765")
        await asyncio.Future()  

asyncio.run(main())