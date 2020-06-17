import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105'
r = requests.get(url)
html = r.content

soup = BeautifulSoup(html, 'html.parser')
#titles = soup.find("div", {"class": "nclicks(fls.list)"})
ul = soup.find('ul', {'class': 'type06_headline'})
lis = ul.find_all('li')

for item in lis:
    title = item.find('img')['alt']
    #link = item.find('a')['href']

    #text_list = [title, link]

#print(text_list)