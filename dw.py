import requests
from bs4 import BeautifulSoup



url='https://www.dw.com/bn/%E0%A6%B8%E0%A7%8C%E0%A6%A6%E0%A6%BF-%E0%A6%86%E0%A6%B0%E0%A6%AC-%E0%A6%87%E0%A6%B8%E0%A6%B0%E0%A6%BE%E0%A7%9F%E0%A7%87%E0%A6%B2-%E0%A6%9A%E0%A7%81%E0%A7%8D%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%BF-%E0%A6%AE%E0%A6%A7%E0%A7%8D%E0%A6%AF%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%9A%E0%A7%8D%E0%A6%AF%E0%A6%95%E0%A7%87-%E0%A6%95%E0%A7%80-%E0%A6%A6%E0%A7%87%E0%A6%AC%E0%A7%87/a-66939544'
response=requests.get(url)

if response.status_code == 200:
    soup=BeautifulSoup(response.text,'html.parser')
    links=soup.find_all('a',class_='sc-hLclGa ekhgcl link-in-teaser')
    for link in links:
        href=link.get('href')
        print(href)