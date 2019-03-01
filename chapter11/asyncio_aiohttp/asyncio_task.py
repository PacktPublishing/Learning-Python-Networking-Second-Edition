#!/usr/bin/python3

import asyncio
import time

@asyncio.coroutine
def task_sleep(name, loop, seconds=1):
        future = loop.run_in_executor(None, time.sleep, seconds)
        print("[%s] coroutine will sleep for %d second(s)..." % (name, seconds))
        yield from future
        print("[%s] done!" % name)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    tasks = [asyncio.Task(task_sleep('Task-A', loop, 10)),
                asyncio.Task(task_sleep('Task-B', loop,5)),
                asyncio.Task(task_sleep('Task-C', loop))]
      
    loop.run_until_complete(asyncio.gather(*tasks))
