# PS D:\จารแดง\class8-asyncio> & C:/Users/Mik/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/??????/class8-asyncio/5-queue-limit.py
# Wed Aug 23 14:39:48 2023 Consumer: Running
# Wed Aug 23 14:39:48 2023 Producer: Running
# Wed Aug 23 14:39:48 2023 Producer: Running
# Wed Aug 23 14:39:48 2023 Producer: Running
# Wed Aug 23 14:39:48 2023 Producer: Running
# Wed Aug 23 14:39:48 2023 Producer: Running
# Wed Aug 23 14:39:48 2023 >got 0.47808056879508765
# Wed Aug 23 14:39:49 2023 >got 0.666496195977806
# Wed Aug 23 14:39:49 2023 >got 0.752587617819378
# Wed Aug 23 14:39:50 2023 >got 0.2021197988821547
# Wed Aug 23 14:39:50 2023 >got 0.8537351506845086
# Wed Aug 23 14:39:51 2023 >got 0.8061375760396131
# Wed Aug 23 14:39:52 2023 >got 0.5443900462600254
# Wed Aug 23 14:39:52 2023 >got 0.470284011003111
# Wed Aug 23 14:39:53 2023 >got 0.92331267131492
# Wed Aug 23 14:39:54 2023 >got 0.9016035137217348
# Wed Aug 23 14:39:55 2023 >got 0.5128880895804852
# Wed Aug 23 14:39:55 2023 >got 0.40502021200578653
# Wed Aug 23 14:39:56 2023 >got 0.9218027291454741
# Wed Aug 23 14:39:57 2023 >got 0.2033995012356412
# Wed Aug 23 14:39:57 2023 >got 0.505272753668842
# Wed Aug 23 14:39:57 2023 >got 0.33252184040261135
# Wed Aug 23 14:39:58 2023 >got 0.37543512378059885
# Wed Aug 23 14:39:58 2023 >got 0.7065587436181164
# Wed Aug 23 14:39:59 2023 >got 0.04528735496507397
# Wed Aug 23 14:39:59 2023 >got 0.5436343661209583
# Wed Aug 23 14:39:59 2023 >got 0.19846854234676325
# Wed Aug 23 14:40:00 2023 >got 0.5544517319194744
# Wed Aug 23 14:40:00 2023 >got 0.7645791302940104
# Wed Aug 23 14:40:01 2023 >got 0.8470663930755997
# Wed Aug 23 14:40:02 2023 >got 0.574827326695249
# Wed Aug 23 14:40:02 2023 >got 0.30344847596922575
# Wed Aug 23 14:40:03 2023 >got 0.824512164592333
# Wed Aug 23 14:40:03 2023 >got 0.4118627679350939
# Wed Aug 23 14:40:04 2023 >got 0.6997363884274747
# Wed Aug 23 14:40:05 2023 >got 0.844442066618961
# Wed Aug 23 14:40:05 2023 >got 0.2499079483249863
# Wed Aug 23 14:40:06 2023 >got 0.4741547433402553
# Wed Aug 23 14:40:06 2023 >got 0.0025627020415636137
# Wed Aug 23 14:40:06 2023 >got 0.7585870099150327
# Wed Aug 23 14:40:07 2023 >got 0.29802586076358717
# Wed Aug 23 14:40:07 2023 >got 0.8426070267756164
# Wed Aug 23 14:40:08 2023 >got 0.6043211646410819
# Wed Aug 23 14:40:09 2023 >got 0.4963225154562818
# Wed Aug 23 14:40:09 2023 >got 0.35385511642752354
# Wed Aug 23 14:40:10 2023 >got 0.045305579630767645
# Wed Aug 23 14:40:10 2023 Producer: Done
# Wed Aug 23 14:40:10 2023 >got 0.736060709615076
# Wed Aug 23 14:40:10 2023 >got 0.38758601005509663
# Wed Aug 23 14:40:10 2023 Producer: Done
# Wed Aug 23 14:40:11 2023 >got 0.5482559648181068
# Wed Aug 23 14:40:11 2023 Producer: Done
# Wed Aug 23 14:40:11 2023 >got 0.08833895533481739
# Wed Aug 23 14:40:11 2023 >got 0.10461425730938867
# Wed Aug 23 14:40:12 2023 >got 0.5232622494489289
# Wed Aug 23 14:40:12 2023 Producer: Done
# Wed Aug 23 14:40:12 2023 >got 0.11348986197393773
# Wed Aug 23 14:40:12 2023 >got 0.20482555857956863
# Wed Aug 23 14:40:12 2023 >got 0.6143530214341184
# Wed Aug 23 14:40:13 2023 Producer: Done
# Wed Aug 23 14:40:13 2023 >got 0.8262853853892554

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
        # mark as completed
        queue.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())