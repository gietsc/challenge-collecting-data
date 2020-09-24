#CHRIS'S SIDE
from bs4 import BeautifulSoup
import requests

url='https://www.realo.be/en/search/for-sale'
r = requests.get(url)
print(url, r.status_code)
soup = BeautifulSoup(r.content,'lxml')

links=[]
for elem in soup.find_all('a',attrs={"class" :"link"}):
    links.append(elem.get('href'))

links_properties=['https://www.realo.be'+ elem for elem in links]

print(links_properties)

# PLEASE MENTION IN THE GROUP ONCE YOU CHANGE THIS FILE.

#DEMO FROM TOWARDS DATA SCIENCE, USE THIS TO TRY THE ATTRIBUTES

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request
from requests import get
import requests
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

url='https://www.realo.be/en/search/for-sale'
response = get(url, headers=headers)
print(response)
r= requests.get(url)
print(url,r.status_code)
html_soup = BeautifulSoup(response.text, 'html.parser')

print('TADAA')
house_containers = html_soup.find_all('li')
print(house_containers)
print('!!HERE WE ARE!!!')

for tag in html_soup.find_all('div',attrs={"data-type":"label"}):
    prices = list(tag)
    print(prices)
print('!!PRICE TAGS NOT HASHTAGS!!')


