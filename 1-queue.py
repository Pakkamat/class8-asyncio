# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

# Wed Aug 23 14:26:40 2023 Producer: Running
# Wed Aug 23 14:26:40 2023 Consumer: Running
# Wed Aug 23 14:26:40 2023 Producer: put 0.5653920707139913
# Wed Aug 23 14:26:40 2023 >got 0.5653920707139913
# Wed Aug 23 14:26:41 2023 Producer: put 0.6604570547509037
# Wed Aug 23 14:26:41 2023 >got 0.6604570547509037
# Wed Aug 23 14:26:41 2023 Producer: put 0.20492123672792584
# Wed Aug 23 14:26:41 2023 >got 0.20492123672792584
# Wed Aug 23 14:26:42 2023 Producer: put 0.7091922563775875
# Wed Aug 23 14:26:42 2023 >got 0.7091922563775875
# Wed Aug 23 14:26:43 2023 Producer: put 0.9424580876270838
# Wed Aug 23 14:26:43 2023 >got 0.9424580876270838
# Wed Aug 23 14:26:43 2023 Producer: put 0.6738989681668169
# Wed Aug 23 14:26:43 2023 >got 0.6738989681668169
# Wed Aug 23 14:26:44 2023 Producer: put 0.544529680966119
# Wed Aug 23 14:26:44 2023 >got 0.544529680966119
# Wed Aug 23 14:26:44 2023 Producer: put 0.3921601901077887
# Wed Aug 23 14:26:44 2023 >got 0.3921601901077887
# Wed Aug 23 14:26:45 2023 Producer: put 0.932883969462454
# Wed Aug 23 14:26:45 2023 >got 0.932883969462454
# Wed Aug 23 14:26:46 2023 Producer: put 0.2993165778221174
# Wed Aug 23 14:26:46 2023 Producer: Done
# Wed Aug 23 14:26:46 2023 >got 0.2993165778221174
# Wed Aug 23 14:26:46 2023 Consumer: Done

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
        print(f'{time.ctime()} Producer: put {value}')
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')

# coroutie to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal
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