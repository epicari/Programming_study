import requests
from bs4 import BeautifulSoup

url = 'https://stockplus.com/m/news/latest'
r = requests.get(url)
html = r.content

soup = BeautifulSoup(html, 'html.parser')
#titles = soup.select('.section_body > div > div > a')
#search = soup.select('newsList')
#titles = search.find_all('a')
#search = soup.find_all('span')
link = soup.a
for parent in link.parents:
    print(parent.name)