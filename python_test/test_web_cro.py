import requests
from bs4 import BeautifulSoup

url = 'https://m.clien.net/service/'
r = requests.get(url)
html = r.content

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.section_body > div > div > a')

with open('clien.csv', 'w') as file: #csv 파일로 내보내기
    file.write('title\n')
    for i in range(len(titles)):
        #print(i+1, titles[i].text)
        file.write('{0}\n'.format(titles[i].text))
