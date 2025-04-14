import requests,csv,os
from bs4 import BeautifulSoup

os.system("cls")

with open("all_qoutes.csv","w", newline="", encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["Qoute","Author","tag"])

    base_url="https://quotes.toscrape.com"
    url="/page/1/"

    while url:
        print(f"Scraping {base_url+url}...")
        res=requests.get(base_url+url)
        soup=BeautifulSoup(res.text,"html.parser")

        qoutes=soup.find_all("div",class_="qoute")

        for qoute in qoutes:
            text=soup.find("span", class_="text").text
            author=soup.find("small", class_="author").text
            tag=soup.find("a",class_="tag").text.strip()

            writer.writerow([text,author,tag])


        next_btn =soup.find("li",class_="next")
        if next_btn:
            url=next_btn.a['href']
        else:
            url=None

print("seccess")