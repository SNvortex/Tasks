import requests
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update({
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
})

url = 'https://www.gethatch.com/en/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for brand in soup.find_all('img', attrs={'class': r'qode_client_main_image'}):
    if brand.get('data-lazy-src') is not None:
        print(brand.get('data-lazy-src'))
