from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS  # BeautifulSoup is a Python library
# for pulling data out of HTML and XML files.

import urllib.request
import urllib.parse
import urllib.error
import ssl
import re
import pandas as pd
import np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import seaborn as sns
import requests
from bs4 import BeautifulSoup




ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count=1 # for pagination
locality=[]
typeofproperty=[]
price=[]
numberofrooms=[]
kitchenfullyequipped=[]
area=[]
furnished=[]
openfire=[]
surface_of_the_land=[]
Surface_area_of_the_plot_of_land=[]
number_of_facade=[]
swimming_pool=[]
state_of_the_building=[]
url = ["https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE"]
for x in url:
    count = 1
    y = x
    while (count < 5):  # will go till 4 pages
        print(x)
for tag in soup.findAll('div', attrs={'data-testid': 'property-price'}):  # gets rent
    row = tag.get_text()
    if not row:
        row = "NA"
    print(row)
    locality.append(row)

    # for tag in soup.findAll('div',attrs={'class':'Text__TextBase-sc-1i9uasc-0-div Text__TextContainerBase-sc-1i9uasc-1 lcNNgu'}): #gets add
    # row = tag.get_text()
    # print(row)
    # address.append(row)



for tag in soup.findAll('div', attrs={'data-testid': 'property-street'}):
    row = tag.get_text()
    if not row:
        row = "NA"
    print(row)
    typeofproperty.append(row)


for tag in soup.findAll('div', attrs={'data-testid': 'property-beds'}):
    row = tag.get_text()
    if not row:
        row = "NA"
    print(row)
    price.append(row)

for tag in soup.findAll('div', attrs={'data-testid': 'property-baths'}):
    row = tag.get_text()
    if not row:
        row = "NA"
    print(row)
    numberofrooms.append(row)

for tag in soup.findAll('div', attrs={'data-testid': 'property-floorSpace'}):
    row = tag.get_text()
    if not row:
        row = "NA"
    print(row)
    kitchenfullyequipped.append(row)

for tag in soup.findAll('div', attrs={'data-testid': 'property-floorSpace'}):
    row = tag.get_text()
    if not row:
        row = "NA"
    print(row)
    area.append(row)

    links = []
    for cards in soup.findAll('div', attrs={
        'class': 'Box-sc-8ox7qa-0 jIGxjA PropertyCard__PropertyCardContainer-sc-1ush98q-2 gKJaNz'}):

        for link in cards.findAll('a', attrs={'href': re.compile("^/")}):
            links.append("https://www.trulia.com" + link.get('href'))  # appends all links in the page

    # print(links) # picking up each link and reading inside it
for link in links:
        addr_link.append(link)
        req = Request(link, headers=get_headers())
        htmlfile = urlopen(req)
        htmltext = htmlfile.read()
        # print (htmltext)
        soup = BS(htmltext, 'html.parser')  # Reads inside links
        # print("hello")


for tag in soup.findAll('span',attrs={'class': 'Text__TextBase-sc-1i9uasc-0 fOuqJu'}):
            row = tag.get_text()
            if not row:
                row = "NA"
            print(row)
            furnished.append(row)

for tag in soup.findAll('div', attrs={'data-testid': 'explore-the-area-commuteTab'}):
            row = tag.get_text()
            if not row:
                row = "NA"
            print(row)
            openfire.append(row)  # commute

for tag in soup.findAll('div', attrs={'data-testid': 'seo-description-paragraph'}):
            row = tag.get_text()
            if not row:
            print(row)
            descp.append(row)  # commute

for tag in soup.findAll('div', attrs={'data-testid': 'explore-the-area-commuteTab'}):
            row = tag.get_text()
            if not row:
                row = "NA"
            print(row)
            surface_of_the_land.append(row)  # commute
for tag in soup.findAll('div', attrs={'data-testid': 'explore-the-area-commuteTab'}):
            row = tag.get_text()
            if not row:
                row = "NA"
            print(row)
            Surface_area_of_the_plot_of_land.append(row)  # commute
for tag in soup.findAll('div', attrs={'data-testid': 'explore-the-area-commuteTab'}):
            row = tag.get_text()
            if not row:
                row = "NA"
            print(row)
            number_of_facade.append(row)  # commute
for tag in soup.findAll('div', attrs={'data-testid': 'explore-the-area-commuteTab'}):
                row = tag.get_text()
                if not row:
                    row = "NA"
                print(row)
                swimming_pool.append(row)  # commute
for tag in soup.findAll('div', attrs={'data-testid': 'explore-the-area-commuteTab'}):
                    row = tag.get_text()
                    if not row:
                        row = "NA"
                    print(row)
                    state_of_the_building.append(row)
        # add more code here
    count = count + 1
    page = str(count) + "_p"  # changes page,will go till page 4,total 120 links per city
    x = y + page
data_frame = pd.DataFrame(
    list(zip(locality, typeofproperty, price, numberofrooms, kitchenfullyequipped, area, furnished, openfire, surface_of_the_land, Surface_area_of_the_plot_of_land, number_of_facade,swimming_pool,state_of_the_building)),
    columns=["Locality", "Type of Property", "Price", "Number of Rooms", "Kitchen Fully Equipped", "Area", "Furnished", "Open Fire", "Surface of the Land", "Surface Area of the Plot of Land", "Number of Facade","Swimming Pool","State of the Building"])
data_frame




