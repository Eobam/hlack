import asyncio
import websockets as wso

clients = set()

async def handle(ws):
    clients.add(ws)
    try:
        async for msg in ws:
            await asyncio.gather(*[
                c.send(msg) for c in clients if c != ws
            ])
    except wso.exceptions.ConnectionClosed:
        pass
    finally:
        clients.remove(ws)

async def main():
    async with wso.serve(handle, "localhost", 6789):
        print("ws://localhost:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())