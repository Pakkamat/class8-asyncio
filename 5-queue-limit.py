# Wed Aug 23 15:13:25 2023 Consumer: Running
# Wed Aug 23 15:13:25 2023 Producer: Running
# Wed Aug 23 15:13:25 2023 Producer: Running
# Wed Aug 23 15:13:25 2023 Producer: Running
# Wed Aug 23 15:13:25 2023 Producer: Running
# Wed Aug 23 15:13:25 2023 Producer: Running
# Wed Aug 23 15:13:25 2023 > got 0.7529183165523943
# Wed Aug 23 15:13:26 2023 > got 0.4290354675427862
# Wed Aug 23 15:13:27 2023 > got 0.9254700019875749
# Wed Aug 23 15:13:28 2023 > got 0.6420604759758715
# Wed Aug 23 15:13:28 2023 > got 0.8889281904914739
# Wed Aug 23 15:13:29 2023 > got 0.4217705530040282
# Wed Aug 23 15:13:30 2023 > got 0.2567719410947926
# Wed Aug 23 15:13:30 2023 > got 0.38754793609204363
# Wed Aug 23 15:13:30 2023 > got 0.7489006323078319
# Wed Aug 23 15:13:31 2023 > got 0.10447778569588717
# Wed Aug 23 15:13:31 2023 > got 0.8192200698131186
# Wed Aug 23 15:13:32 2023 > got 0.34039176383764025
# Wed Aug 23 15:13:32 2023 > got 0.9837695675103615
# Wed Aug 23 15:13:33 2023 > got 0.846189910825048
# Wed Aug 23 15:13:34 2023 > got 0.39329130244459864
# Wed Aug 23 15:13:35 2023 > got 0.28680792781661213
# Wed Aug 23 15:13:35 2023 > got 0.028036372451095692
# Wed Aug 23 15:13:35 2023 > got 0.0746636237698185
# Wed Aug 23 15:13:35 2023 > got 0.7219687368654295
# Wed Aug 23 15:13:36 2023 > got 0.19221894363007586
# Wed Aug 23 15:13:36 2023 > got 0.34440379906219987
# Wed Aug 23 15:13:36 2023 > got 0.8550280649758994
# Wed Aug 23 15:13:37 2023 > got 0.6173631838396029
# Wed Aug 23 15:13:38 2023 > got 0.9760624221363784
# Wed Aug 23 15:13:39 2023 > got 0.803696593208714
# Wed Aug 23 15:13:40 2023 > got 0.16982550901210836
# Wed Aug 23 15:13:40 2023 > got 0.5140271403942018
# Wed Aug 23 15:13:40 2023 > got 0.02556118078475378
# Wed Aug 23 15:13:40 2023 > got 0.07975963206675352
# Wed Aug 23 15:13:40 2023 > got 0.7396738704054681
# Wed Aug 23 15:13:41 2023 > got 0.6851323642907611
# Wed Aug 23 15:13:42 2023 > got 0.2924520962307092
# Wed Aug 23 15:13:42 2023 > got 0.8674652291586448
# Wed Aug 23 15:13:43 2023 > got 0.903631790252753
# Wed Aug 23 15:13:44 2023 > got 0.11887593601035018
# Wed Aug 23 15:13:44 2023 > got 0.5901131533878173
# Wed Aug 23 15:13:45 2023 > got 0.12084625489739709
# Wed Aug 23 15:13:45 2023 Producer 1: Done
# Wed Aug 23 15:13:45 2023 > got 0.6218130894969806
# Wed Aug 23 15:13:45 2023 > got 0.024073169917304793
# Wed Aug 23 15:13:45 2023 > got 0.320703090658387
# Wed Aug 23 15:13:45 2023 Producer 2: Done
# Wed Aug 23 15:13:46 2023 > got 0.0008636285351431017
# Wed Aug 23 15:13:46 2023 > got 0.8445994656269187
# Wed Aug 23 15:13:47 2023 > got 0.30950333798564933
# Wed Aug 23 15:13:47 2023 > got 0.5392195031600131
# Wed Aug 23 15:13:47 2023 > got 0.8322115600089472
# Wed Aug 23 15:13:48 2023 > got 0.9801209857116906
# Wed Aug 23 15:13:48 2023 Producer 3: Done
# Wed Aug 23 15:13:49 2023 > got 0.38651869259613647
# Wed Aug 23 15:13:49 2023 Producer 4: Done
# Wed Aug 23 15:13:50 2023 > got 0.1624729861646096
# Wed Aug 23 15:13:50 2023 Producer 5: Done
# Wed Aug 23 15:13:50 2023 > got 0.47812488553004506
# Wed Aug 23 15:13:50 2023 > got 0.9921333556973604

from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue, id):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep((id + 1)*0.1)
        # add to the queue 
        await queue.put(value)
    print(f'{time.ctime()} Producer {id+1}: Done') 

# coroutie to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work 
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark the task as done 
        queue.task_done()
    # all done 
    print(f'{time.ctime()} Consumer: Done')

#entry point coroutine
async def main():
    # create a shared queue 
    queue = asyncio.Queue(2)
    # start consumer 
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue, i) for i in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # run the producer and consumer 
    await queue.join()


#start the asyncio program
asyncio.run(main())