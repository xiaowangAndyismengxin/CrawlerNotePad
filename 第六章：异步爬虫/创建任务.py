import asyncio
import random


async def return_randint_number(num):
    print("Number:", num)
    return num + random.randint(0, 99)


def callback(t: asyncio.Task):
    print("Result:", t.result())


coroutine = return_randint_number(1)
print("Coroutine:", coroutine)

try:
    loop = asyncio.new_event_loop()

    # loop.run_until_complete(coroutine)

    # task = loop.create_task(coroutine)
    task = asyncio.ensure_future(coroutine, loop=loop)

    task.add_done_callback(callback)
    print("Task:", task)
    loop.run_until_complete(task)
    print("Task:", task)
    print("Task result:", task.result())
finally:
    try:
        loop.close()
    except NameError:
        ...
