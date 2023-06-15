import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://www.capitoltrades.com/trades"

# Send a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object with the webpage content
soup = BeautifulSoup(response.content, "html.parser")

# Find and extract specific data from the webpage
paragraphs = soup.find_all("p")
tag = soup.body

# Print the extracted data
for p in paragraphs:
  if p.text[:9] == 'Page 1 of':
    #print('Pages: ' + p.text[10:14])
    pages = int(p.text[10:14])

# data starts at 42
# each item is 16 length
# 12 rows
listy=[]
tmp = 0
for string in tag.strings:
  if tmp == 234:
    break
  if tmp >= 41:
    listy.append(string)
  tmp=tmp+1

for x in range(100):
  url = "https://www.capitoltrades.com/trades?page=" + "x+2"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  tmp = 0
  for string in tag.strings:
    if tmp == 234:
      break
    if tmp >= 42:
      listy.append(string)
    tmp=tmp+1



df = pd.DataFrame(columns=['Name', 'Party', 'Job', 'State', 'Company', 'Stock', 'Date', 'Time', 'Year', 'Date2', 'days', 'filed_after', 'Owner', 'buy/sell', 'Size', 'Price'])
column_names = df.columns
row_dict = {}

for i in range(0, len(listy), len(column_names)):
    row_values = listy[i:i + len(column_names)]
    row_dict = dict(zip(column_names, row_values))
    df = df.append(row_dict, ignore_index=True)

df.to_csv('data.csv', index=False)
