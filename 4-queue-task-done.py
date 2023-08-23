# Wed Aug 23 14:36:39 2023 Consumer: Running
# Wed Aug 23 14:36:39 2023 Producer: Running
# Wed Aug 23 14:36:39 2023 >got 0.04998824184872008
# Wed Aug 23 14:36:39 2023 >got 0.26799675878506013
# Wed Aug 23 14:36:40 2023 >got 0.4992998123904998
# Wed Aug 23 14:36:40 2023 >got 0.5991331746794196
# Wed Aug 23 14:36:41 2023 >got 0.5397072735156165
# Wed Aug 23 14:36:42 2023 >got 0.29987709953599473
# Wed Aug 23 14:36:42 2023 >got 0.9783873562514369
# Wed Aug 23 14:36:43 2023 >got 0.7773838189480786
# Wed Aug 23 14:36:44 2023 Producer: Done
# Wed Aug 23 14:36:44 2023 >got 0.4800872380805945
# Wed Aug 23 14:36:44 2023 >got 0.03812108202045206

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
    print(f'{time.ctime()} Producer: Done')

# coroutie to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # retrieve the get() awaitable
        item = await queue.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item :
            await asyncio.sleep(item)
        # mark the task as done
        queue.task_done()

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    await asyncio.create_task(producer(queue))
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())