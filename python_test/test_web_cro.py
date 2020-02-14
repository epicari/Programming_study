import requests, csv
from bs4 import BeautifulSoup

url = 'https://m.clien.net/service/'
r = requests.get(url)
html = r.content

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.section_body > div > div > a')

with open('clien.csv', 'w', newline='') as csvfile: #csv 파일로 내보내기
    filednames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=filednames)

    writer.writeheader()
    writer.writerow({'first_name': })



# CSV module이 존재함
# https://docs.python.org/3/library/csv.html
