from bs4 import BeautifulSoup
import requests
from random import randint
from time import sleep
import xlwt
from xlwt import Workbook


url = "https://myanimelist.net/topanime.php?limit=1450"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

ranking = doc.find_all(class_="ranking-list")

# rank = ranking[30].a
# print(rank.get('href'))

# rank = ranking[30].a
# file1 = open("MAL.html", "a")  # append mode
# file1.write(rank.get('href') + "\n")
# file1.close()

fname = "MAL2.html"

with open(fname, "a", encoding="utf-8") as f: 

    for x in range(50):
        sleep(randint(1,5))
        
        rank = ranking[x].a
        f.write('"' + rank.get('href') +'"' + ", " + "\n" )
        
f.close()
