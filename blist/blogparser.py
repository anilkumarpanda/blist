# Code to parse blog posts
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

class BlogParser:

    def __init__(self, url):
        self.url = url
        self.root = _get_root_url(self.url)
        self.headers = {
            "User-Agent":
                "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
        }

    def _get_root_url(url):
        return urlparse(url).netloc

    def get_blog_posts(self):
        result = requests.get(self.url, headers=self.headers)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        for a in soup.find_all('a', href=True):
            print(f"Found the URL: {self.root}/{a['href']}")