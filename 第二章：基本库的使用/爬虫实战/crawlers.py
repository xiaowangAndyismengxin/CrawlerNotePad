import requests
import re
import logging
from urllib.parse import urljoin
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s ----- %(levelname)s: %(message)s"
)
logging.captureWarnings(True)


class SSR1Crawler:
    def __init__(self, verity: bool = True, disable_requests_warnings: bool = False):
        if disable_requests_warnings:
            requests.urllib3.disable_warnings()
        self.VERITY: bool = verity

    def get_detail_page_url(self) -> list:
        page: int = 1
        url_pattern: re.Pattern[str] = re.compile(r'<a [^>]*?href="([^"]*?)"[^>]*?class="name">')
        url_list: list = list()
        while True:
            url = f'https://ssr1.scrape.center/page/{page}'
            resp = requests.get(url, verify=self.VERITY)
            if resp.status_code == 500:
                logging.info('index out of page')
                break
            text = resp.text
            url_list_np: list = re.findall(url_pattern, text)
            if url_list_np is None:
                logging.error(f'\"None" when scraping index page {page}')
            url_list.extend([urljoin(url, path) for path in url_list_np])
            logging.info(f'finish index page {page}')
            page += 1
        return url_list

    def parse_detail(self, url_list: list | None = None) -> dict[str: dict[str: str | float | None]]:
        if url_list is None:
            url_list: list[str] = self.get_detail_page_url()

        parse_dict: dict[str: dict[str: str | float | None]] = dict()

        cover_pattern: re.Pattern[str] = re.compile(r'<img[^>]*?src="([^"]*)"[^>]*?class="cover"')
        name_pattern: re.Pattern[str] = re.compile(r'<h2[^>]*?class="m-b-sm">(.*?)</h2>', re.S)
        categories_pattern: re.Pattern[str] = re.compile(r'<button[^>]*?category.*?<span>(.*?)</span>.*?</button>',
                                                         re.S)
        published_at_pattern: re.Pattern[str] = re.compile(r'(\d{4})-(\d{2})-(\d{2})\s*?上映')
        drama_pattern: re.Pattern[str] = re.compile(r'剧情简介</h3>.*?<p.*?>(.*?)</p>', re.S)
        score_pattern: re.Pattern[str] = re.compile(r'<p[^>]*?class="score[^"]*">(.*?)</p>', re.S)

        for url in url_list:
            logging.info(f'Strat parsing {url}')
            resp = requests.get(url, verify=self.VERITY)
            if resp.status_code != 200:
                logging.error(f'bad status code {resp.status_code} when scraping {url}')
                continue
            text = resp.text
            try:
                cover = re.search(cover_pattern, text).group(1).strip('\n \t')
            except AttributeError:
                cover = None
            except TypeError:
                cover = None

            try:
                name = re.search(name_pattern, text).group(1).strip('\n \t')
            except AttributeError:
                name = None
            except TypeError:
                name = None

            try:
                categories = [c.strip('\n \t') for c in re.findall(categories_pattern, text)]
            except AttributeError:
                categories = None
            except TypeError:
                categories = None

            try:
                pa_res = re.search(published_at_pattern, text)
                published_at = {
                    'month': int(pa_res.group(2).strip('\n \t')),
                    'day': int(pa_res.group(3).strip('\n \t')),
                    'year': int(pa_res.group(1).strip('\n \t'))
                }
            except AttributeError:
                published_at = {
                    'month': None,
                    'day': None,
                    'year': None
                }
            except TypeError:
                published_at = {
                    'month': None,
                    'day': None,
                    'year': None
                }

            try:
                drama = re.search(drama_pattern, text).group(1).strip('\n \t')
            except AttributeError:
                drama = None
            except TypeError:
                drama = None

            try:
                score = float(re.search(score_pattern, text).group(1).strip('\n \t'))
            except AttributeError:
                score = None
            except TypeError:
                score = None

            parse_dict[url] = {
                "cover": cover,
                "name": name,
                "categories": categories,
                'published_at': published_at,
                'drama': drama,
                'score': score
            }
            logging.info(f'Parsed {url}')
        return parse_dict

    def save_data(self, film_dict: dict[str: dict[str: str | float | None]] | None = None,
                  dir_name: str = 'results', auto_replace_illegal_character: bool = True) -> None:
        if film_dict is None:
            film_dict = self.parse_detail()
        for film_url, film_detail in film_dict.items():
            file_name = f'{film_detail['name']}.json'
            if auto_replace_illegal_character:
                file_name = (file_name
                             .replace('\\', '')
                             .replace('/', '')
                             .replace(':', '')
                             .replace('*', '')
                             .replace('?', '')
                             .replace('<', '')
                             .replace('>', '')
                             .replace('|', ''))
            with open(f'{dir_name}/{file_name}', 'w', encoding='utf-8') as f:
                json.dump({film_url: film_detail}, f, ensure_ascii=False, indent=2)
            logging.info(f'save {file_name} successfully')
        logging.info('save all successfully')
