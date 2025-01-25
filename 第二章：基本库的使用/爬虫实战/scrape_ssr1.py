import requests
import re
import logging
from urllib.parse import urljoin

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s ----- %(levelname)s: %(message)s"
)
logging.captureWarnings(True)
requests.urllib3.disable_warnings()
GET_VERITY = False


class SSR1Crawler:
    def scrape_index_page_url(self) -> list:
        page = 1
        url_pattern = re.compile(r'<a [^>]*?href="([^"]*?)"[^>]*?class="name">', re.S)
        url_list = list()
        while True:
            url = f'https://ssr1.scrape.center/page/{page}'
            resp = requests.get(url, verify=GET_VERITY)
            if resp.status_code == 500:
                logging.info('index out of page')
                break
            text = resp.text
            url_list_np = re.findall(url_pattern, text)
            if url_list_np is None:
                logging.error(f'\"None" when scraping index page {page}')
            url_list.extend([urljoin(url, path) for path in url_list_np])
            logging.info(f'finish index page {page}')
            page += 1
        return url_list


crawler = SSR1Crawler()
print(crawler.scrape_index_page_url()
