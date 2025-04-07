import requests
from bs4 import BeautifulSoup

URL = "https://www.boomplay.com/lyrics/167797552"
response  = requests.get(URL)

soup = BeautifulSoup(response .content, "html.parser")

quotes = soup.find_all('div', {'class': 'lyrics'})

for quote in quotes:
   paragraph = quote.findChildren('p')
   for paragrap in paragraph:
      print(paragrap.text)


    


