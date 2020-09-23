from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request

url= 'https://www.realo.be/en/search-be'
r= requests.get(url)
print(url,r.status_code)
soup = BeautifulSoup(r.content,'lxml')
print(soup.prettify())


# PLEASE MENTION IN THE GROUP ONCE YOU CHANGE THIS FILE.