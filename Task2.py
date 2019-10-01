import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.gethatch.com/en/')
soup = BeautifulSoup(response.content, 'html.parser')

for brand in soup.find_all('img', attrs={'class': r'qode_client_main_image'}):
    if brand.get('data-lazy-src') is not None:
        print(brand.get('data-lazy-src'))
