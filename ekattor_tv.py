#text-left black--text text-h5 text-sm-h4 text-md-h3 mb-0 mb-sm-3


import requests
from bs4 import BeautifulSoup
import time


cnt=0
#url='https://ekattor.tv/politics/51429/%E0%A6%B0%E0%A6%BE%E0%A6%B7%E0%A7%8D%E0%A6%9F%E0%A7%8D%E0%A6%B0%E0%A6%AF%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0-%E0%A6%A8%E0%A6%BF%E0%A6%B0%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%A4%E0%A6%A8%E0%A7%87%E0%A6%B0-%E0%A6%95%E0%A6%BE%E0%A6%B0%E0%A6%96%E0%A6%BE%E0%A6%A8%E0%A6%BE'
url='https://ekattor.tv/international/51893/%E0%A6%AA%E0%A6%BE%E0%A6%95%E0%A6%BF%E0%A6%B8%E0%A7%8D%E0%A6%A4%E0%A6%BE%E0%A6%A8%E0%A7%87-%E0%A6%86%E0%A6%A4%E0%A7%8D%E0%A6%AE%E0%A6%98%E0%A6%BE%E0%A6%A4%E0%A7%80-%E0%A6%AC%E0%A7%8B%E0%A6%AE%E0%A6%BE-%E0%A6%AC%E0%A6%BF%E0%A6%B8%E0%A7%8D%E0%A6%AB%E0%A7%8B%E0%A6%B0%E0%A6%A3-%E0%A6%A8%E0%A6%BF%E0%A6%B9%E0%A6%A4-%E0%A7%AB%E0%A7%A6'

final=[url]
while cnt<5000:
    if(cnt%300==0 and cnt>0):
        time.sleep(60)
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find and extract the titles of articles
        article_titles = soup.find('h1',class_='title')
        links=soup.find_all('a',class_='link_overlay')
        if links:
            with open('links.txt','a') as file:
                for link in links:
                    href=link.get('href')
                    # file.write(href+'\n')
                    href='https:'+href
                    if(href not in final):
                        final.append(href)


        with open('output.txt', 'a', encoding='utf-8') as file:
            for title in article_titles:
                file.write(str(cnt)+"\t"+title.text+'\n\n')
            file.write('\n\n')


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)

    cnt+=1
    if(cnt==len(final)):
        prev_len=len(final)
        temp=0

        while temp-prev_len<100 and temp<len(final):
            url=final[temp]
            response=requests.get(url)
            if response.status_code == 200:
                soup=BeautifulSoup(response.text,'html.parser')
                links=soup.find_all('a',class_='link_overlay')
                if links:
                    for link in links:
                        href=link.get('href')
                        # file.write(href+'\n')
                        href='https:'+href
                        if(href not in final):
                            final.append(href)
            temp+=1
            print("crawling at: "+str(temp))


    if cnt<len(final[cnt]):
        url=final[cnt]
        
    print(cnt,len(final))


