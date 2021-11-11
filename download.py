from bs4 import BeautifulSoup, SoupStrainer
import requests
import os

# url dos dados abertos
url = 'http://200.152.38.155/CNPJ/'
# confure pasta para download e logs, configure rota completa
path_download = '<path>/download'

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)

links=[]
for link in soup.find_all('a'):
    if str(link.get('href')).endswith('.zip'): 
        cam = link.get('href')
        if not cam.startswith('http'):
            links.append(url+cam)

i=0
for link in links:
    # print(link) # printe para verificar os links
    i=i+1
    os.system("wget -c -b {} '{}'  > log_{}.log &".format(link, path_download, i))

# monitorar downloads
os.system("watch 'ls -lh .'")
