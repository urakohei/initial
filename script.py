import requests
import time
import csv
from bs4 import BeautifulSoup
import re
#import pandas as pd
import datetime
import sys

word = input("にゅーりょく")
keyword_list = [i for i in word.split(' ')]

def replace_n(str_data):
    return str_data.replace('\n', '').replace('\r', '')
def concat_list(list_data):
    str_data = ''
    for j in range(len(list_data)):
        str_data = str_data + replace_n(list_data[j].getText()) + ' , '
    return str_data
output_data = []
output_data.append(['検索順位', 'title', 'url', 'description', 'h1', 'h2'])

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
responce = requests.get('https://www.google.co.jp/search?num=20&q=' + ' '.join(keyword_list), headers=headers)
time.sleep(5)
responce.raise_for_status()
h1_text = ''
h2_text =''
soup = BeautifulSoup(responce.text, 'html.parser')
entries = soup.find_all("div", class_ = "rc")
for title in entries:
   title_text = title.find("h3").text
   url_text = title.find("a")["href"]
   description_text = title.find("div", class_="s").text
   #print(title_text)
   #print(url_text)
   #print(description_text)
   res = requests.get(url_text, headers = headers)
   time.sleep(2)
   sp = BeautifulSoup(res.text, "html.parser")
   if sp.find("h1"):
       h1_text = sp.find("h1")
       #print(h1_text)

   if sp.find("h2"):
       h2_text = sp.find("h2")
       #print(h2_text)
   # print(h1_text)
   # print(h2_text)
   output_data_new = title_text, url_text, description_text, h1_text, h2_text
   output_data.append(output_data_new)


now = datetime.datetime.now()
mojiretsu = ','.join(keyword_list)
csv_file = open('[' + mojiretsu + ']' + '{0:%Y%m%d%H%M%S}'.format(now) + '.csv', 'w', encoding='UTF-8_sig')
csv_writer = csv.writer(csv_file, lineterminator='\n')
for j in range(len(output_data)):
    csv_writer.writerow(output_data[j])
csv_file.close()

testtesttestttestestestest
