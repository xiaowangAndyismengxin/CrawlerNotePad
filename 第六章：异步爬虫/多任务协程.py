import asyncio


async def get_square(num):
    return num**2


def callback(t: asyncio.Task):
    print("Result:", t.result())


loop = asyncio.new_event_loop()
tasks = [asyncio.ensure_future(get_square(num), loop=loop) for num in range(10)]
for task in tasks:
    task.add_done_callback(callback)

loop.run_until_complete(asyncio.wait(tasks))
# loop.run_until_complete(asyncio.gather(*tasks))
