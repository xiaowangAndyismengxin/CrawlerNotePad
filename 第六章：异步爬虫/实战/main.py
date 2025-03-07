from crawler import AsyncScrapeSPA5
import asyncio


crawler = AsyncScrapeSPA5(503, 5, default_delay=15)
asyncio.run(crawler.save_data())
