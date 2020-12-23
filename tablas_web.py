"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://mike.larsson.es/es/search/734.20.78/in/all/article/493539")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class":"show_history_tips"})[0]
rows = table.findAll("tr")

with open("editors.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    for row in rows:
        csv_row = []
        for cell in row.findAll(["td", "th"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)
"""
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen

html = urlopen("https://mike.larsson.es/es/search/734.20.78/in/all/article/493539")
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table")
output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([output_rows])