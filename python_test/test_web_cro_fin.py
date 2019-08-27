import requests
from bs4 import BeautifulSoup

def fin(code, page_num):
    result = [[], [], []]

    for i in range(page_num):
        
        url = 'https://finance.naver.com/item/sise_day.nhn?code='+code+'&page='+str(i+1)
        
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        tr = soup.select('table > tr')

        for j in range(1, len(tr)-1):
            if tr[j].select('td')[0].text.strip():
                result[0].append(tr[j].select('td')[0].text.strip())
                result[1].append(tr[j].select('td')[1].text.strip())
                result[2].append(tr[j].select('td')[6].text.strip())

    for k in range(len(result[0])):
        print(result[0][k], result[1][k], result[2][k])    

code = '005930'
page_num = 10

fin(code, page_num)