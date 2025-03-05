from crawler import AsyncScrapeSPA5
import asyncio


crawler = AsyncScrapeSPA5(10, 3, default_delay=15)
asyncio.run(crawler.save_data())
