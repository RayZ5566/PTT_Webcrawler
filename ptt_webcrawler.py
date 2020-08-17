# -*- coding: utf-8 -*-
"""webcrawler.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YI8W8TQ1Q9ED4SXAksw7uXQTvSGtmTqL
"""

pip install beautifulsoup4

pip install requests_html

import requests
import pandas_datareader as web
from bs4 import BeautifulSoup as bs
from requests_html import HTML
import pprint
import re
import matplotlib.pyplot as plt

def fetch(url):
  result = requests.get(url, cookies={'over18': '1'})
  return result
url = "https://www.ptt.cc/bbs/LoL/M.1597046974.A.EC6.html"
res = fetch(url)
print(res.text)

from requests_html import HTML

def parse(doc):
  html = HTML(html = doc)
  post_entries = html.find('div.push')
  return post_entries

url = "https://www.ptt.cc/bbs/LoL/M.1597046974.A.EC6.html"
res = fetch(url)
post_entries = parse(res.text)

print(post_entries)

def extract(entry):
  return {'f3.hl.push-userid': entry.find('.push-userid', first=True).text,
      'f3.push-content': entry.find('.push-content', first=True).text
    }
cont = {}
for entry in post_entries:
    meta = extract(entry)
    #print(meta)
    cont['{}'.format(meta['f3.hl.push-userid'])] = meta['f3.push-content'].replace(': ','')
for k, v in cont.items():
  print(k,':',v)

playoff_clubs = ['TES','SN','FPX','IG','JDG','WE','V5','LGD']

for club in playoff_clubs:
  for entry in post_entries: 
    meta = extract(entry)
    #filtered all pushes without team included 
    if club in meta['f3.push-content'] or \
      club.lower() in meta['f3.push-content'] or \
      club.title() in meta['f3.push-content']: 
      print(meta['f3.hl.push-userid'],':',meta['f3.push-content'].replace(': ',''))
      
      #cont['{}'.format(meta['f3.hl.push-userid'])] = meta['f3.push-content'].replace(': ','')

cont ={}
for club in playoff_clubs:
  for entry in post_entries: 
    meta = extract(entry)
    #filtered all pushes without team included 
    if club in meta['f3.push-content'] or \
      club.lower() in meta['f3.push-content'] or \
      club.title() in meta['f3.push-content']:
      pushes = meta['f3.push-content'].replace(': ','') #removing ': '
      pushes = pushes.encode('ascii', 'ignore').decode() #removing chinese characters
      regex = re.compile('[,\.!?=]') #removing non-characters
      pushes = regex.sub(' ', pushes)
      print(meta['f3.hl.push-userid'],':',pushes)
      
      cont['{}'.format(meta['f3.hl.push-userid'])] = pushes

cont['jevin']

team_dict = dict.fromkeys(playoff_clubs, 0)
print(team_dict)

team_dict = dict.fromkeys(playoff_clubs, 0)
print(team_dict)
for club in playoff_clubs:
  for entry in post_entries: 
    meta = extract(entry)
    #filtered all pushes without team included 
    if club in meta['f3.push-content'] or \
      club.lower() in meta['f3.push-content'] or \
      club.title() in meta['f3.push-content']:
      team_dict[club] += 1
print(team_dict)

sort_orders = sorted(team_dict.items(), key=lambda x: x[1], reverse=True)
order_team ={}
for i in sort_orders:
  order_team['{}'.format(i[0])] = i[1]
print(order_team)

keys = order_team.keys()
values = order_team.values()

plt.bar(keys, values)
plt.title('mvp team')

string_with_nonASCII = "àa string withé fuünny charactersß."

encoded_string = string_with_nonASCII.encode("ascii", "ignore")
decode_string = encoded_string.decode()

print(encoded_string)
print(decode_string)

t = sorted(team_dict.values(), reverse=True)
print(t)





