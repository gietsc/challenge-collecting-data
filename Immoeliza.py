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
