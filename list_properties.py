from bs4 import BeautifulSoup
import requests
import csv 
## This is my code to try to iterate over the pages
#url_list = []
#number_list = []
#number = 0

#while number < 11:
#    number += 1
#    number_list.append(number)

#for num in number_list:
#    url_list.append(url + str(num))

#print(len(url_list))

#for url in url_list:
##Code to iterate over pages ending here

url = "https://www.realo.be/en/search/for-sale?page=1"
r = requests.get(url)
soup = BeautifulSoup(r.content,'lxml')

links=[]
for elem in soup.find_all('a',attrs={"class" :"link"}):
    links.append(elem.get('href'))

links_properties=['https://www.realo.be'+ elem for elem in links]

##This is the code to export the URL's in a CSV file
#with open('mytest.csv', 'w') as f: 
    # using csv.writer method from CSV package 
  #  write = csv.writer(f) 
      
  #  write.writerow(links_properties) 