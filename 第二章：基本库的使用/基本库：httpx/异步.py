import httpx
import asyncio


async def r(url):
    async with httpx.AsyncClient() as c:
        await c.get(url)
        print('ok')


async def main():
    url = 'https://www.httpbin.org/get'
    tasks = [asyncio.ensure_future(r(url)) for _ in range(50)]
    await asyncio.gather(*tasks)


asyncio.run(main())
