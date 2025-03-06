import json
import logging
from asyncio import gather
from logging import info, warning, error
import asyncio
import motor.motor_asyncio
import aiohttp
import tqdm

# 创建根logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 创建文件处理器
file_handler = logging.FileHandler("ScrapeSPA5.log")
file_handler.setFormatter(logging.Formatter('%(asctime)s --- %(levelname)s: %(message)s'))

# 创建控制台处理器
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(logging.Formatter('%(asctime)s --- %(levelname)s: %(message)s'))

# 添加处理器
logger.addHandler(file_handler)


# logger.addHandler(console_handler)


class AsyncScrapeSPA5:
    def __init__(self, page_limit: int, concurrency: int, page_size: int = 18,
                 default_delay: int = 5, timeout: int = 10):
        self.page_limit = page_limit
        self.semaphore = asyncio.Semaphore(concurrency)
        self.page_size = page_size
        self.default_delay = default_delay
        self.index_api = ("https://spa5.scrape.center/api/book/?limit={limit}"
                          "&offset={offset}")
        self.detail_api = "https://spa5.scrape.center/api/book/{book_id}/"
        self.aiohttp_timeout = aiohttp.ClientTimeout(total=timeout)

    async def scrape_api(self, url, turn_json=True, fault_list=None) -> \
            (dict | None | str):
        async with self.semaphore:
            try:
                async with aiohttp.ClientSession(timeout=self.aiohttp_timeout) as session:
                    async with session.get(url) as resp:
                        info(f'Scraping {url}...')

                        if resp.status != 200:
                            warning(f'Bad status code {resp.status} when scraping '
                                    f'{url}')

                            fault_list.append(url)
                            return None

                        if turn_json:
                            try:
                                return await resp.json()
                            except json.JSONDecodeError:
                                error("Can't decode web as json.",
                                      exc_info=True)
                                fault_list.append(url)
                                return None

                        return await resp.text()
            except (json.JSONDecodeError, aiohttp.ClientError, asyncio.TimeoutError):
                error("Something wrong!", exc_info=True)
                fault_list.append(url)
                return None

    def get_index_api(self) -> list:
        return [self.index_api.format(limit=self.page_size,
                                      offset=self.page_size * (page - 1))
                for page in range(1, self.page_limit + 1)]

    def get_detail_api(self, ids: list[int]) -> list:
        return [self.detail_api.format(book_id=book_id) for book_id in ids]

    async def _retry_scrape(self, urls, *, tqdm_desc, delay=None):
        with tqdm.tqdm(total=len(urls), desc=tqdm_desc) as pbar:
            if delay is None:
                delay = self.default_delay

            fault_list = []
            tasks = []
            for url in urls:
                task = asyncio.ensure_future(self.scrape_api(url, fault_list=fault_list))
                task.add_done_callback(lambda t: pbar.update(1))
                tasks.append(task)

            results = await asyncio.gather(*tasks)

        while fault_list:
            info('Sleeping~~')
            await asyncio.sleep(delay)
            info('Wake up.')

            with tqdm.tqdm(total=len(fault_list), desc=tqdm_desc + ': retry') as pbar:
                fault_list_copy = fault_list.copy()
                fault_list.clear()
                for url in fault_list_copy:
                    task = asyncio.ensure_future(self.scrape_api(url, fault_list=fault_list))
                    task.add_done_callback(lambda t: pbar.update(1))
                    tasks.append(task)

                results.extend(await asyncio.gather(*tasks))

        results = [item for item in results if item is not None]
        return results

    async def get_ids(self, delay=None):

        results = await self._retry_scrape(self.get_index_api(), tqdm_desc='Get ids', delay=delay)
        ids = [book['id']
               for result in results
               for book in result['results']]

        return ids

    async def get_detail(self, delay=None):
        ids = await self.get_ids(delay)
        results = await self._retry_scrape(self.get_detail_api(ids), tqdm_desc='Get detail', delay=delay)
        return results

    def start_scraping(self, delay=None):
        info("Starting scraping process...")
        try:
            result = asyncio.run(self.get_detail(delay))
            info("Scraping completed successfully")
            return result
        except Exception:
            error("Scraping failed", exc_info=True)
            raise

    async def save_data(self, connection_string='mongodb://localhost:27017',
                        db_name='crawler', collection_name='books'):
        results = await self.get_detail()

        client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
        db = client[db_name]
        collection = db[collection_name]

        tasks = []
        for book in results:
            info(f'Add data task id {book.get('id')}')
            if book:
                task = asyncio.ensure_future(collection.update_one(
                    {'_id': book.get('id')},
                    {'$set': book},
                    upsert=True
                ))
                tasks.append(task)
            else:
                warning('Book data is empty!')
                continue

        if tasks:
            info('start to save all data...')
            await gather(*tasks)
            info('All data saved.')
