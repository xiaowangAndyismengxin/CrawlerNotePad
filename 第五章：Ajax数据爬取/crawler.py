# 使用XHR过滤出所有的Ajax请求
from typing import Callable, Any
import requests
import logging
import pymongo


logging.basicConfig(
    filename="ScrapeSPA1.log",
    format='%(asctime)s --- %(levelname)s: %(message)s',
    level=logging.INFO
)


class ScrapeSPA1:
    def __init__(self, scrape_count: int = 100) -> None:
        self.request_url = (f"https://spa1.scrape.center/api/movie/"
                            f"?limit={scrape_count}&offset=0")

    def scrape_api(self, url, turn_json=True) -> dict | None | str:
        logging.info(f'Scraping {url}...')

        try:
            resp = requests.get(url)
        except requests.RequestException:
            logging.error(f"Something Wrong when scraping {url}.",
                          exc_info=True)
            return None

        if resp.status_code != 200:
            logging.warning(f'Bad status code {resp.status_code} when scraping '
                            f'{url}')
            return None

        if turn_json:
            try:
                return resp.json()
            except requests.JSONDecodeError:
                logging.error("Can't decode web as json.", exc_info=True)
                return None

        return resp.text

    def scrape_index(self) -> dict | None:
        return self.scrape_api(self.request_url)

    def _get_default_no_args(self, function_name: Callable[[], Any]) -> Any:
        data = function_name()
        if data is None:
            logging.warning(f"Can't get anything from {function_name.__name__}.")
        return data

    def get_detail_api(self, data: dict | None = None) -> None | set[str]:
        if not data:
            data = self._get_default_no_args(self.scrape_index)
            if data is None:
                return None

        if not (results := data.get('results')):
            logging.warning('"results" not in detail data.')
            return None

        detail_api = set()
        for film in results:
            film_id = film.get('id')
            if film_id:
                api_url = f'https://spa1.scrape.center/api/movie/{film_id}/'
                detail_api.add(api_url)
            else:
                logging.warning(f'Get unknown id {film_id} in {film}.')

        if not detail_api:
            logging.warning(f'Get no id from {results}.')
            return None

        return detail_api

    def scrape_detail(self, api_url: dict[str] | set[str] | None = None,
                      return_sorted: bool = True) -> None | list[dict | None]:
        if not api_url:
            api_url = self._get_default_no_args(self.get_detail_api)
            if api_url is None:
                return None

        detail_data = []

        for url in api_url:
            data = self.scrape_api(url)
            if not data:
                logging.warning(f"Can't get anything from {url}")
                detail_data.append(None)

            else:
                detail_data.append(data)

        if not detail_data:
            logging.warning("Can't get anything from detail")
            return None

        if return_sorted:
            detail_data.sort(key=lambda x: x.get('id', 0) if x else 0)

        return detail_data

    def save(self, data: list | None = None,
             connect_string: str = 'mongodb://localhost:27017',
             db_name: str = 'crawler', collection_name: str = 'movies') -> None:
        if not data:
            data = self._get_default_no_args(self.scrape_detail)
            if data is None:
                return None

        with pymongo.MongoClient(connect_string) as client:
            db = client[db_name]
            collection = db[collection_name]

            for film in data:
                collection.update_one(
                    {'_id': film['id']},
                    {'$set': film},
                    upsert=True
                )
                logging.info(f'Film id: {film['id']} save ok.')
