import requests
from bs4 import BeautifulSoup
import time


url1='https://www.ittefaq.com.bd/'
cnt=15817


while True:
    url=url1+str(cnt)+"/"
    print(cnt)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        h1=soup.find('h1',class_='title mb10')
        contents=soup.find('div',class_='viewport jw_article_body')
        category=soup.find('h2',class_='secondary_logo')
        date=soup.find('div',class_='each_row time')
        tags=soup.find('div',class_='topic_list')
        if h1 and contents:
            # titles
            h1=h1.text




            # contents
            contents=contents.find_all('span')
            content=str()
            for x in contents:
                content+=x.text
            # print(content)



            # category
            category=category.find('span')
            # print(category.text)





            # time
            date=date.find('span',class_='tts_time')
            # print(date.text)





            # tags
            tags=tags.find_all('strong')
            tag=str()
            for x in tags:
                tag+=x.text
                if x!=tag[-1]:
                    tag+=', '
            
            # print(tag)



    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
        
    
    cnt+=1
    break
    if cnt%2000==0:
        time.sleep(100)
    



