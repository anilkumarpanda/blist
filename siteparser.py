from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

headers = {
    "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
}

websites = [
    'https://sebastianraschka.com/blog',
    'https://manassaloi.com/posts/',
    'https://huyenchip.com/blog/',
    'http://www.paulgraham.com/articles.html',
    'https://chrisrempel.com/',
    'https://xiaoxiaowang87.github.io/',
    'https://randsinrepose.com/archives/',
    'https://invertedpassion.com/',
    ]
# website = f'{root}/movies'


def get_root_url(url):
    return urlparse(url).netloc

for website in websites:

    result = requests.get(website,headers=headers)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    root = get_root_url(website)
    for a in soup.find_all('a', href=True):
        print (f"Found the URL: {root}/{a['href']}")