import requests
import random
from bs4 import BeautifulSoup


def get_first_news():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.52'
    }

    url = 'https://www.anekdot.ru/random/anekdot/'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    anecdot = soup.find_all('div', class_="text")
    anekdot_list = []
    for article in anecdot:
        anekdot_list.append(article.text.strip())

    print(random.choice(anekdot_list))


get_first_news()
