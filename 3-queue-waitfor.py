# Wed Aug 23 14:27:28 2023 Producer: Running
# Wed Aug 23 14:27:28 2023 Consumer: Running
# Wed Aug 23 14:27:28 2023 >got 0.2389507943861835
# Wed Aug 23 14:27:28 2023 >got 0.21196795626474685
# Wed Aug 23 14:27:28 2023 >got 0.08273960937772307
# Wed Aug 23 14:27:29 2023 >got 0.3195233096439918
# Wed Aug 23 14:27:29 2023 Consumer: gave up waitting...
# Wed Aug 23 14:27:29 2023 >got 0.5966157015436654
# Wed Aug 23 14:27:29 2023 >got 0.04293367992893227
# Wed Aug 23 14:27:30 2023 Consumer: gave up waitting...
# Wed Aug 23 14:27:30 2023 >got 0.9441439848865025
# Wed Aug 23 14:27:31 2023 Consumer: gave up waitting...
# Wed Aug 23 14:27:31 2023 >got 0.781255475672943
# Wed Aug 23 14:27:31 2023 >got 0.3707229718134192
# Wed Aug 23 14:27:32 2023 Consumer: gave up waitting...
# Wed Aug 23 14:27:32 2023 Producer: Done
# Wed Aug 23 14:27:32 2023 >got 0.5463328138098869
# Wed Aug 23 14:27:32 2023 Consumer: Done

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
        # get a unit of work
        try:
            # retrieve the get() awaitable
            get_await = queue.get()
            # await the awaitable with a time out
            item = await asyncio.wait_for(get_await, 0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waitting...')
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