import sys 
import trio 

# need to run echo-server.py first 

PORT = 12345 

async def sender(client_stream): 
    print("sender: start")
    while True: 
        data = b"this is part of the plan"
        print(f"sender: sending {data!r}")
        await client_stream.send_all(data)
        await trio.sleep(1)

async def receiver(client_stream): 
    print("receiver: start")
    async for data in client_stream: 
        print(f"receiver: got data {data!r}")
    print("receiver: connection close")
    sys.exit()

async def parent(): 
    print(f"parent: connecting to 127.0.0.1:{PORT}")
    client_stream = await trio.open_tcp_stream("127.0.0.1", PORT)
    async with client_stream: 
        async with trio.open_nursery() as nusery: 
            print("parent: spawn sender")
            nusery.start_soon(sender, client_stream)

            print("parent: spawn receiver")
            nusery.start_soon(receiver, client_stream)

if __name__ == "__main__": 
    trio.run(parent)

