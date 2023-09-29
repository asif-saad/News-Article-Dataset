import requests
from bs4 import BeautifulSoup


url1='https://ekattor.tv/'
cnt=1587


while True:
    url=url1+str(cnt)+"/"
    print(cnt)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h1=soup.find('h1',class_='title')
        if h1:
            h1=h1.text
            print(h1)


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    cnt+=1
    







