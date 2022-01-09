import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.metal-archives.com/bands/%5BFür%5D/3540417998'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

cnt = soup.find_all('div', {"id":"band_tabs"})

print(cnt)