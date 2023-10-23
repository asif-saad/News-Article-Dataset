#text-left black--text text-h5 text-sm-h4 text-md-h3 mb-0 mb-sm-3


import requests
from bs4 import BeautifulSoup


cnt=500282
url1='https://www.banglatribune.com/'

with open('C:/Users/asifs/OneDrive/Desktop/News-Article-Dataset/Ittefaq/output.txt', 'a', encoding='utf-8') as file:
    while True:
        url=url1+str(cnt)+'/'


        response = requests.get(url)
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')
            tag=soup.find('span')
            if(tag.text!='404 - Not Found'):
                file.write(str(cnt)+'\n')
                #break



        else: 
            print('Failed to retrieve the web page. Status code:', response.status_code)
        

        cnt+=1
        print(cnt)
    
