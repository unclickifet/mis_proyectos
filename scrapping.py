import urllib.request
from bs4 import BeautifulSoup

#Url de destino
url = 'https://mike.larsson.es/es/search/734.20.78/in/all/article/493539'

# Usamos request para abrir la URL
ourUrl = urllib.request.urlopen(url)

# Creamos a BeatifulSoup objeto, 
soup = BeautifulSoup(ourUrl, 'html.parser')

# Ver lo que hay dentro de SOUP
print(soup.prettify())

# Creamos lista vacia de la tienda
review=[]

results = soup.find(id='order-opc')
print(soup.prettify())
len(review)



