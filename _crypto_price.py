import requests
from bs4 import BeautifulSoup

URL = "https://www.forbes.com/sites/digital-assets/2025/04/06/existential-threat-wall-street-suddenly-braced-for-a-bitcoin-and-crypto-price-game-changer/"
response  = requests.get(URL)

soup = BeautifulSoup(response .content, "html.parser")

paragraph = soup.find_all('p')

for paragrap in paragraph:
   print(paragrap.text)