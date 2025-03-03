import aiohttp
import asyncio
import time


start = time.time()

async def get_delay_5():
    try:
        url = 'https://www.httpbin.org/delay/5'
        time_out = aiohttp.ClientTimeout(total=100)
        async with aiohttp.ClientSession(timeout=time_out) as session:
            response = await session.get(url)
            print(url + ':', response)
        return response
    except asyncio.TimeoutError:
        print('Time out!')


loop = asyncio.new_event_loop()
tasks = [asyncio.ensure_future(get_delay_5(), loop=loop) for _ in range(10)]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

end = time.time()
spend_time = end - start
print('time:', spend_time)
