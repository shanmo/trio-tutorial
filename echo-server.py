import trio 
from itertools import count 

PORT = 12345

CONNETION_COUNTER = count()

async def echo_server(server_stream): 
    ident = next(CONNETION_COUNTER)
    print(f"echo_server {ident}: start")
    try: 
        async for data in server_stream: 
            print(f"echo_server {ident}: received data {data!r}")
            await server_stream.send_all(data)
        print(f"echo_server {ident}: connection closed")
    except Exception as exc:
        print(f"echo_server {ident}: crashed: {exc!r}")

async def main(): 
    await trio.serve_tcp(echo_server, PORT)

if __name__ == "__main__": 
    trio.run(main)
        