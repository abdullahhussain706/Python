#qoutes web scrap and start scrapping

import os,csv
import requests
from bs4 import BeautifulSoup

os.system("cls")

url="https://quotes.toscrape.com/"
response=requests.get(url)

print(response.status_code)

soup=BeautifulSoup(response.text, "html.parser")
qoutes=soup.find_all("span",class_="text")
authors=soup.find_all("small", class_="author")
tags=soup.find_all("a",class_="tag")

with open("qoutes.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["Qoute","Author","Tag"])

    for qoute, author, tag in zip(qoutes,authors,tags):
        writer.writerow([qoute.text,author.text,tag.text.strip()])

print("Created successfully!")
