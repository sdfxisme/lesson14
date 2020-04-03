# Ищем отзовы, имена и даты на пилу "Stihl 250" на двух сайтах

from bs4 import BeautifulSoup
import requests
import csv
import re
URL= 'https://vse-otzivi.ru/product/stihl-ms-250-otzyvy/'
URL1 = 'https://nanegative.ru/stihl-ms-250-otzivy'
page = requests.get(URL)
page1 = requests.get(URL1)

print(page1.status_code)
print(page.status_code)

soup1 = BeautifulSoup(page1.text, 'html.parser')
soup = BeautifulSoup(page.text, 'html.parser')

reviews = soup.find_all('div', class_ = 'cm_single_comment_dignity_ins')
user_user = soup.find_all('span', class_ = 'cm_single_comment_name')
date = soup.find_all('span', class_ = 'cm_single_comment_date')

reviews1 = soup1.find_all('td', itemprop='reviewBody')
user_user1 = soup1.find_all('span', itemprop='author')
date1 = soup1.find_all('meta', itemprop='datePublished') #не знаю как отсюда дату вытащить

rev_plus = []
rev_user = []
rev_date = []

for i in reviews:
    rev_plus.append(i.text)
for i in user_user:
    rev_user.append(i.text)
for i in date:
    rev_date.append(i.text)

for i in reviews1:
   rev_plus.append(i.text)
for i in user_user1:
    rev_user.append(i.text)
for i in date1:
    rev_date.append(i.text)

print(len(rev_plus),len(rev_user),len(rev_date))
otzovi = [rev_plus, rev_user, rev_date]
print(otzovi)

with open('otzovi.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(otzovi)

with open('otzovi.csv','r') as f:
    reader = csv.reader(f)
for row in reader:
    print(row)


