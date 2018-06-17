import urllib.request
import json
from bs4 import BeautifulSoup
import re

ab_kodu = input("Abonent kodunuz: ")
api_url = "https://opendata.e-gov.az/api/v1/json/azersu/DebtInfo/{}".format(ab_kodu)

with urllib.request.urlopen(api_url) as url:
    output = url.read().decode('utf-8')
    data = json.loads(output)

html = data['Response']['HtmlField']
soup = BeautifulSoup(html, "html.parser")
l = []

for a in soup.find_all('b'):
    l.append(re.sub(r"[<b>,</b>]", "", str(a)))

kod = l[1]
ad = l[3]
borc = l[5]
print("Abonentin kodu: {}\nAdi: {}\nBorc: {}".format(kod,ad,borc))
