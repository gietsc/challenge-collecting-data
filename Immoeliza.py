#All our packages required for the project
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request
from requests import get
import requests

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

#Variables
price=[]
typeofproperty=[]
locality=[]
n_pages=0

#This is our loop to go through all the pages of the website
for page in range(0,2):
    n_pages+=1
    url= 'https://www.realo.be/en/search/for-sale?page='+str(page)
    req= get(url, headers=headers)
    html_soup = BeautifulSoup(req.text, 'html.parser')

    house_containers = html_soup.find_all('li')

    #This is our loop to append our "Price" list
    for tag in html_soup.find_all('div',attrs={"data-type":"label"}):
        row = tag.get_text()
        price.append(row)

    #This is our loop to append our "Property type" list
    for elem in html_soup.find_all('span',attrs={"class":"type truncate"}):
        type = list(elem)
        types = [n.strip() for n in type]
        typeofproperty.append(types)

    #This is our loop to append our "Address" list
    for n in html_soup.find_all('div',attrs={"class":"address truncate"}):
        local= [n.text]
        locals = [i.strip() for i in local]
        locality.append(locals)

print(len(locality))
print(len(price))
print(len(typeofproperty))
