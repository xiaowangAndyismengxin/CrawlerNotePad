import aiohttp
import asyncio
import time


CONCURRENCY = 5
start = time.time()
semaphore = asyncio.Semaphore(CONCURRENCY)


async def get_delay_5():
    async with semaphore:
        try:
            url = "https://www.httpbin.org/delay/5"
            time_out = aiohttp.ClientTimeout(total=100)
            async with aiohttp.ClientSession(timeout=time_out) as session:
                response = await session.get(url)
                print(url + ":", response)
            return response
        except asyncio.TimeoutError:
            print("Time out!")


async def main():
    tasks = [asyncio.ensure_future(get_delay_5()) for _ in range(10)]
    results = await asyncio.gather(*tasks)
    # print(results)


asyncio.run(main())
end = time.time()
print("Time:", end - start)
