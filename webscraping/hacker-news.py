import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
votes = soup.select('.score')


def custom_hn(links, votes):
    hn = []
    for idx, m in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href')
        # hn.append({'tittle': title, 'link': href})
        hn.append(href)
    return hn

print(custom_hn(links, votes))