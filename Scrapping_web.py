
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup  #BeautifulSoup is a Python library
                                    #for pulling data out of HTML and XML files.
import csv
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
import pdb
import requests

with open('myurllist-2.csv', 'r') as f:
    urls = next(csv.reader(f))
    #urls = list(csv.reader(f))


# print(urls[0])
# print(urls[1])
# pdb.set_trace()


############"
#####  TO DO....................
#############
#ask christope for correct links, I will scap
urls=urls[0:5]





# "https://www.trulia.com/for_rent/Oakland,CA/1p_beds/SINGLE-FAMILY_HOME_type
# url="https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE"
#url=urls[0][0]  #get the url from Christope list

#Note: when we have a list of urls, Beautifulsoup gives an error to overcome this problem,
# we have either use get_headers or urllib.request (this is not working), so I need to try with urllib3 later
def get_headers():
    #Headers
    headers={'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language':'en-US,en;q=0.9',
            'cache-control':'max-age=0',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

    return headers

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


locality=[] #ok
typeofproperty=[] #ok
price=[]
numberofrooms=[]  #ok
kitchenfullyequipped=[]
area=[]
furnished=[]
openfire=[]
Surface_area_of_the_plot_of_land=[]
swimming_pool=[]
state_of_the_building=[]
Open_fire=[] #(Yes / No)
Terrace=[]#(Yes / No) If yes: Area
Area_of_Terrace=[]
Garden=[]#(Yes/No)
Area_of_Garden=[]#If yes: Area
Surface_of_Land=[]
Surface_area_of_PlotLand=[]
Number_of_facades=[]
Swimming_pool=[]#(Yes / No)
State_of_Building=[]  #(New, to be renovated, ...)



# for url in urls: #extract from te csv file
# count=1 # for pagination





#soup = BS(htmltext,'html.parser')

print("------------------------------")
print("------------------------------")
print("------------------------------")
print("------------------------------")
# urls=[urls[0][0], urls[1][0]]

for url in urls:
    print(url)
    # Note: I will scrap first from only the first page, to be sure about the result
    req = Request(url, headers=get_headers())  # req all headers
    htmlfile = urlopen(req)
    htmltext = htmlfile.read()


    r = requests.get(url)
    print(url, r.status_code)
    soup = BeautifulSoup(r.content,'html.parser')

    container = soup.find_all('div', attrs={"class":"property__container"})
    for c in container:  #price, locality, from Dilara
            for link in c.findAll('h1', attrs={'class':"address"}):
             # print(link.text)
              locality.append(link.text.strip())

    for c in container:  #price, locality, type of property from Dilara
            for link in c.findAll("span", attrs={"itemprop":"price"}):
             # print(link.text)
              price.append(link.text)

    table = soup.find_all("table")
    #print(table[1])
    #to iterate for all tables
    # for each_table in table:
    #     print(each_table.find("tbody"))
    #     print("----------------------------")

    #I want only table[1] to scrap it

    table = soup.find_all("table")
    rows=table[1]
    a=[]

    # for item in rows.find_all("tr"):
    #     for sub_item in item.find_all("td"):
    #          a.append(sub_item.text.strip().replace(',',''))

    results = {}
    for item in rows.find_all("tr"):
        aux = item.findAll('td')
        results[aux[0].string] = aux[1].string

    #print (results)
    # for k, v in results.items():
    #     print(k, v)
    #appending to lists:
    if results['Property type'] !=None:
        typeofproperty.append(results['Property type'].strip())

    if 'Bedrooms' in results: #we have land for sale, so there is no bedroom key
        numberofrooms.append(results['Bedrooms'])
    else:
        numberofrooms.append(0)

#{ 'Bathrooms': '1',
# 'Habitable area': None,
# 'Facade width': '9,3m',
# 'Lot size': None,
# '\n\t\t\t\t\tBackside/Garden orientation\n\t\t\t\t': '\n\t\t\t\t\tWest\n\t\t\t\t',
# 'Year built': '1972',
# 'Year renovated': '2015',
# 'Building placement': '\n\t\t\t\tTerraced\n\t\t\t',
# 'Heating type': '\n\t\t\t\t\tGas\n\t\t\t\t',
# 'Garages': '1',
# 'Cadastral income': '€ 430',
# 'Electrical inspection report': '\n\t\t\t\t\tAvailable, conform\n\t\t\t\t',
# 'Planning permit': '\n\t\t\t\t\tYes\n\t\t\t\t',
# 'Subdivision permit': '\n\t\t\t\t\tNo\n\t\t\t\t',
# 'Summons issued': '\n\t\t\t\t\tNo\n\t\t\t\t',
# 'Pre-emption': '\n\t\t\t\t\tYes\n\t\t\t\t',
# 'Flood-prone area': '\n\t\t\t\t\tNot in flood-prone area\n\t\t\t\t'}

print("------------------------------------")
print(locality)
print(typeofproperty)
print(price)
print(numberofrooms)

