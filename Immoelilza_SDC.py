# All our packages required for the project
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request
from requests import get
import requests
import pdb
import re
import pandas as pd

headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

# Variables

price = []
type_of_property = []
locality= []
city= []
bed_rooms = []
bath_rooms = []
area = []
n_pages = 0

# This is our loop to go through all the pages of the website
for page in range(0, 2):
    n_pages += 1
    url = 'https://www.realo.be/en/search/for-sale?page=' + str(page)
    req = get(url, headers=headers)


    html_soup = BeautifulSoup(req.text, 'html.parser')

    house_containers = html_soup.find_all('li')
    #####################################################
    #  "Price" list
    ####################################################
    for p in html_soup.find_all('div', attrs={"data-type": "label"}):
        price.append(re.findall(r'\d+', p.text)[0])
        #print(re.findall(r'\d+', p.text)[0])
        #pdb.set_trace()

    #####################################################
    #  "Postal Code" list
    ####################################################
    for pc in html_soup.find_all('div', attrs={"class": "address truncate"}):
        if pc.text.strip()!=None:
            locality.append(re.findall(r'\d{4}', pc.text)[0])
        else:
            locality.append('None')

    #####################################################
    #  "City" list
    ####################################################
    for m in html_soup.find_all('div', attrs={"class": "address truncate"}):
        if m.text.strip()!=None:
            city.append(re.findall(r'\D+.?\w+$', m.text)[0])
        else:
            city.append('None')

    #####################################################
    #  Type of property list
    ####################################################
    for t in html_soup.find_all('div', attrs={'class': 'ways-types truncate'}):
        if t.text.strip()!=None:
            type_of_property +=[t.text.partition(' ')[0].strip()]
        else:
            type_of_property += ['None']


    for c in html_soup.find_all('div', attrs={"class":"details truncate"}):
        lst=[]
        for stat in c.find_all('span'):
            lst.append(stat['class'])
        #     print((stat['class']))
        #     print(lst)

    #####################################################
    #  Bed rooms list
    ####################################################
    for x in html_soup.find_all('span', attrs={"class": "icon icn-dot beds"}):
        if ['icon', 'icn-dot', 'beds'] in lst: #we have room

          bed_rooms.append((x.text)[0])
        else:
            bed_rooms.append("N.A")

    #####################################################
    #  Bath rooms list
    ####################################################
    for c in html_soup.find_all('span', attrs={"class": "icon icn-dot baths"}):
        if ['icon', 'icn-dot', 'baths'] in lst:  # we have room
            bath_rooms.append((c.text)[0])
        else:
            bath_rooms.append("N.A")
    #####################################################
    #  area list
    ####################################################
    for b in html_soup.find_all('span', attrs={"class": "icon icn-dot area"}):
        if ['icon', 'icn-dot', 'area'] in lst:  # we have room
            area.append((b.text)[0])
        else:
            area.append("N.A")

print(len(city))
print(len(locality))
print(len(price))
print(len(type_of_property))
print(len(bed_rooms))
print(len(bath_rooms))
print(len(area))

#create a data frame
dic={'Property_type':type_of_property,
     'City':city,
     'locality':locality,
     'Price':price,
     #'Bed_rooms':bed_rooms,
     #'Bath_rooms':bath_rooms,
     #'Area':area
     }

df=pd.DataFrame(dic)
#print(df.head(2))
#pdb.set_trace()
df.to_csv('RealStateData.csv', encoding='utf-8', index=False)
