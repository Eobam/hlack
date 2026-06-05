import asyncio
import websockets as wso
import threading



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

def give_html():
    import http.server, socketserver
    with socketserver.TCPServer(("", 8000), SimpleHTTPRequestHandler) as httpd:
        httpd.serve_forever()

        
async def main():
    async with wso.serve(handle, "localhost", 8080):
        print("ws://localhost:8080")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())