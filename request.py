import requests
from bs4 import BeautifulSoup

def req():
    url = 'https://www.e1.ru/text/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    news = soup.find_all('h2', class_='h9Jmx')
    dates = soup.find_all('div', class_='Hiu4B vx3Rq')
    all_news = []
    for quote,date in zip(news,dates):
        all_news.append(date.text)
        all_news.append(quote.text)
        s = url + quote.find('a').get('href')
        all_news.append(s.replace('text//','',1))

    return all_news