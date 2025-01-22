import requests
from bs4 import BeautifulSoup
import csv
url="https://en.wikipedia.org/wiki/Wikipedia:About"
req=requests.get(url)

bs=BeautifulSoup(req.text,"html.parser")

with open("wikipedia_links_name.csv","w",newline="", encoding="utf-8") as csvfile:
    csvdata=csv.writer(csvfile)

    csvdata.writerow(["Name","Link"])

    for link in bs.find_all('a'):
        name=link.text.strip()
        href=link.get('href')

        if name and href:
            full_url = requests.compat.urljoin(url, href)
            csvdata.writerow([name,full_url])
        
print("successful")

