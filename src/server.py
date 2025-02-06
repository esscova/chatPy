import asyncio
import websockets

conexoes = set()  # conexoes ativas
historico = []    # histórico de mensagens

async def chat(websocket):
    conexoes.add(websocket)
    print(f"Novo cliente conectado! Total de clientes: {len(conexoes)}")

    try:
        nome = await websocket.recv()
        print(f"{nome} entrou no chat.")

        for msg in historico:
            await websocket.send(msg)

        entrada_msg = f"[Sistema] {nome} entrou no chat."
        historico.append(entrada_msg)
        for conexao in conexoes:
            await conexao.send(entrada_msg)

        async for mensagem in websocket:
            msg_formatada = f"[{nome}] {mensagem}"
            print(msg_formatada)
            historico.append(msg_formatada)

            for conexao in conexoes:
                await conexao.send(msg_formatada)

    except websockets.exceptions.ConnectionClosedError:
        print(f"{nome} desconectou.")
    finally:
        conexoes.remove(websocket)
        saida_msg = f"[Sistema] {nome} saiu do chat."
        historico.append(saida_msg)
        for conexao in conexoes:
            await conexao.send(saida_msg)
        print(f"{nome} desconectado. Total de clientes: {len(conexoes)}")

async def main():
    async with websockets.serve(chat, "localhost", 8765):
        print("Servidor de chat WebSocket iniciado em ws://localhost:8765")
        await asyncio.Future() 

asyncio.run(main())