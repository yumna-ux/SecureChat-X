import asyncio
import websockets
from crypto import encrypt_message, decrypt_message


async def send(ws):
    loop = asyncio.get_event_loop()
    while True:
        msg = await loop.run_in_executor(None, input)
        if msg == "/exit":
            break
        await ws.send(encrypt_message(msg))


async def receive(ws):
    while True:
        try:
            encrypted = await ws.recv()
            print(decrypt_message(encrypted))
        except:
            break


async def chat():
    async with websockets.connect("ws://localhost:6789") as ws:

        # ---- AUTH ----
        print(await ws.recv())
        await ws.send(input().strip().upper())

        print(await ws.recv())
        await ws.send(input().strip())

        print(await ws.recv())
        await ws.send(input().strip())

        result = await ws.recv()

        if result != "LOGIN_SUCCESS":
            print(result)
            return

        print("Secure chat started.")

        await asyncio.gather(send(ws), receive(ws))


asyncio.run(chat())
