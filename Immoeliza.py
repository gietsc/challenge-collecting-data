from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request
from requests import get
import requests
import pandas as pd
import itertools
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

n_pages=0
for page in range(0,9):
    n_pages+=1
    url= 'https://www.realo.be/en/search/for-sale' +'?page='+str(page)
    req= get(url, headers=headers)
    html_soup = BeautifulSoup(req.text, 'html.parser')


price=[]
typeofproperty=[]
locality=[]

house_containers = html_soup.find_all('li')

for tag in html_soup.find_all('div',attrs={"data-type":"label"}):
    row = tag.get_text()
    if not row:
        row = "NA"

    price.append(row)
print(price)

for elem in html_soup.find_all('span',attrs={"class":"type truncate"}):
    type = list(elem)
    types = [n.strip() for n in type]
    if not types:
        types="NA"
    typeofproperty.append(types)
print(typeofproperty)


for n in html_soup.find_all('div',attrs={"class":"address truncate"}):
    local= [n.text]
    locals = [i.strip() for i in local]
    if not locals:
        locals="NA"
    locality.append(locals)
print(locality)

print(len(locality))
print(len(price))
print(len(typeofproperty))
