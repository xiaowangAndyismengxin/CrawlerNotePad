import requests
from requests.auth import HTTPBasicAuth


r = requests.get('https://ssr3.scrape.center', auth=('admin', 'admin'))
# =
# r = requests.get('https://ssr3.scrape.center', auth=HTTPBasicAuth('admin', 'admin'), verity=VERITY)
print(r.text)
