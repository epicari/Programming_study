import requests
from bs4 import BeautifulSoup

url = 'https://m.clien.net/service/'
r = requests.get(url)
html = r.content

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.section_body > div > div > a > span')

for i in range(len(titles)):
    print(i+1, titles[i].text)