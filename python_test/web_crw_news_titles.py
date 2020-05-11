import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/breakingnews/digital'
r = requests.get(url)
html = r.content

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('div.cont_thumb > strong > a')
for i in range(len(titles)):
    print(titles[i])
# result = <a class="link txt" href="https address"> title </a>
# vue로 보면 링크 달린 타이틀로 변환

