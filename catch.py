import sys
import urllib
import urllib2
import xlwt
from bs4 import BeautifulSoup

stock = sys.argv[1]
begin = sys.argv[2]
end = sys.argv[3]

wb = xlwt.Workbook()
ws = wb.add_sheet('a test sheet')

url = "http://" + stock + ".stock.inv.org.cn/quote/history.php"
values = {
        "type": "daily",
        "begin_day": begin,
        "end_day": end
        }

data = urllib.urlencode(values)

headers={'User-Agent': "Mozilla/5.0"}

req = urllib2.Request(url, data, headers)

response = urllib2.urlopen(req)

page = response.read()

soup = BeautifulSoup(page)
table = soup.table

rows = table.findAll("tr")
x = 0
for tr in rows:
    cols = tr.findAll("td")
    if not cols:
        continue
    y = 0
    for td in cols:
        text_bu = td.text
        text_bu = text_bu.encode("UTF-8")
        text_bu = text_bu.strip()
        ws.write(x, y, td.text)
        #print(x, y, td.text)
        y = y + 1

    x = x + 1

filename = stock + "_" + begin + "_" + end +".xls"
wb.save(filename)
