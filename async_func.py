import trio 
import time

async def child1():
    print("child1: started, sleeping now")
    await trio.sleep(1)
    print("child1: wake up")

async def child2(): 
    print("child2: started, sleeping now")
    await trio.sleep(1)
    print("child2: wake up")

async def parent(): 
    print("parent start")
    async with trio.open_nursery() as nursery: 
        print("parent: spawn child1")
        nursery.start_soon(child1)

        print("parent: spawn child2")
        nursery.start_soon(child2)

        print("parent: waiting")
    print("parent: all done")

if __name__ == "__main__": 
    start = time.time()
    trio.run(parent)
    end = time.time()
    print(f"function takes {end - start} s")
    print("even though there are two trio.sleep(1), total time is still 1s")