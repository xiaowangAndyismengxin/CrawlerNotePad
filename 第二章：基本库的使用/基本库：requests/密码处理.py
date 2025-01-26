import requests
from requests.auth import HTTPBasicAuth


VERITY = False
r = requests.get('https://ssr3.scrape.center', auth=('admin', 'admin'), verify=VERITY)
# =
# r = requests.get('https://ssr3.scrape.center', auth=HTTPBasicAuth('admin', 'admin'), verity=VERITY)
print(r.text)
