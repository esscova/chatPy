import asyncio
import websockets

conexoes = set()

async def chat(websocket, path):
    print(f'Novo cliente conectado: {websocket}\nTotal de conexões: {len(conexoes)}\n')
    conexoes.add(websocket)
   
    try:
        async for message in websocket:
            await broadcast(message)
    finally:
        conexoes.remove(websocket)
        print(f'Cliente desconectado: {websocket}\nTotal de conexões: {len(conexoes)}\n')

async def broadcast(message):
    for conexao in conexoes:
        if conexao != conexoes:
            await conexao.send(message)

async def main ():
    async with websockets.serve(chat, "localhost", 8765):
        print("Servidor iniciado em ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())