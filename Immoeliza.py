#All our packages required for the project
import pandas as pd
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request
from requests import get
import requests

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

#Variables

price = []
typeofproperty = []
locality = []
bedrooms = []
bathrooms=[]
area=[]
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
    #for elem in html_soup.find_all('span',attrs={"class":"type truncate"}):
    #     type = list(elem) #here you create a nested list, this will gives an error in pandas and csv file
     #   types = [n.strip() for n in type]
      #  typeofproperty.append(types)

    # This is our loop to append our "Address" list
    for n in html_soup.find_all('div', attrs={"class": "address truncate"}):
        if n.text.strip()!=None:
            locality.append(n.text.strip())
        else:
            locality.append(None)


    #This is our loop to append our "Address" list
    for n in html_soup.find_all('div',attrs={"class":"address truncate"}):
        local= [n.text]
        locals = [i.strip() for i in local]
        locality.append(locals)

    for x in html_soup.find_all('span', attrs={"class": "icon icn-dot beds"}):
        bedding= [x.text]
        bedrooms.append(bedding)
            
    for c in html_soup.find_all('span', attrs={"class": "icon icn-dot baths"}):
        bathtub= [c.text]
        bathrooms.append(bathtub)
            
    for b in html_soup.find_all('span', attrs={"class": "icon icn-dot area"}):
        land= [b.text]
        area.append(land)

print(len(locality))
print(len(price))
print(len(typeofproperty))
print(len(bedrooms))
print(len(bathrooms))
print(len(area))

#create a data frame
dic={'price':price,
     'typeofproperty':typeofproperty,
     'locality':locality,
     'bedrooms':bedrooms,
     'bathrooms':bathrooms,
     'area':area }

df=pd.DataFrame(dic)
#print(df.head())
df.to_csv('RealStateData.csv', encoding='utf-8', index=False)
