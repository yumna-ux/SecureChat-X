import asyncio
import websockets
from crypto import encrypt_message, decrypt_message
from auth import register_user, authenticate

clients = {}  # websocket -> username


async def handler(ws):
    username = None
    try:
        # ---- AUTH ----
        await ws.send("REGISTER or LOGIN?")
        mode = (await ws.recv()).strip().upper()

        await ws.send("Username:")
        username = (await ws.recv()).strip()

        await ws.send("Password:")
        password = (await ws.recv()).strip()

        if mode == "REGISTER":
            if register_user(username, password):
                await ws.send("Registered. Restart and LOGIN.")
            else:
                await ws.send("Username exists.")
            return

        if not authenticate(username, password):
            await ws.send("Auth failed.")
            return

        clients[ws] = username
        await ws.send("LOGIN_SUCCESS")

        print(username, "connected")

        # ---- CHAT ----
        while True:
            encrypted = await ws.recv()
            message = decrypt_message(encrypted)

            print(f"{username}: {message}")

            broadcast = encrypt_message(f"{username}: {message}")

            # SEND TO ALL CLIENTS
            for client in list(clients):
                if client != ws:
                    await client.send(broadcast)

    except:
        pass

    finally:
        if ws in clients:
            print(clients[ws], "disconnected")
            del clients[ws]


async def main():
    async with websockets.serve(handler, "localhost", 6789):
        print("Server running...")
        await asyncio.Future()

asyncio.run(main())
