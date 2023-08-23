# Wed Aug 23 14:27:04 2023 Producer: Running
# Wed Aug 23 14:27:04 2023 Consumer: Running
# Wed Aug 23 14:27:04 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:04 2023 >got 0.2481225750944298
# Wed Aug 23 14:27:04 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:05 2023 >got 0.32408112450659865
# Wed Aug 23 14:27:05 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:05 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:06 2023 >got 0.9784916390198553
# Wed Aug 23 14:27:06 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:06 2023 >got 0.5745771257614878
# Wed Aug 23 14:27:06 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:07 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:07 2023 >got 0.8835215873603439
# Wed Aug 23 14:27:07 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:08 2023 >got 0.9507421391527361
# Wed Aug 23 14:27:08 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:09 2023 >got 0.06891113118100334
# Wed Aug 23 14:27:09 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:09 2023 >got 0.9798483994975986
# Wed Aug 23 14:27:09 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:10 2023 Consumer: got nothing, waitting a while...
# Wed Aug 23 14:27:10 2023 Producer: Done
# Wed Aug 23 14:27:10 2023 >got 0.6785819400170253
# Wed Aug 23 14:27:10 2023 >got 0.17831466160089982
# Wed Aug 23 14:27:10 2023 Consumer: Done

from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate a value
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')

# coroutie to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waitting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'{time.ctime()} >got {item}')
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())