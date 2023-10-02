import requests
from bs4 import BeautifulSoup
import time

url1='https://ekattor.tv/'
cnt=33800


while True:
    url=url1+str(cnt)+"/"
    print(cnt)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h1=soup.find('h1',class_='title')
        if h1:
            h1=h1.text
            with open('output.txt','a',encoding='utf-8') as file:
                file.write(str(cnt-1587)+'\t'+h1+'\n\n')


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
        
    
    if cnt%300==0:
        time.sleep(100)
    cnt+=1
    







