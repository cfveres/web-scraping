import requests
from bs4 import BeautifulSoup
import pprint

# Requests retrieves the HTML
# BS4 will do the scraping

res = requests.get('https://news.ycombinator.com/news')

# HTML mode specified (HTML <----> XML)

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(news_list):
    return sorted(news_list, key= lambda x:x['votes'], reverse=True)

def create_custom_news(links, votes):
    news = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                news.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(news)

pprint.pprint(create_custom_news(links, subtext))