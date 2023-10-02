import requests
from bs4 import BeautifulSoup


url='https://ekattor.tv/33823'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    h1=soup.find('h1',class_='title')
    category=soup.find('div',class_="breadcrumb")
    div=soup.find('div',class_='viewport jw_article_body')
    tag=soup.find('div',class_='topic_list')
    if h1 and div:
        h1=h1.text
        with open('output.txt','a',encoding='utf-8') as file:
            # category
            if category:
                category=category.find('ul')
                if category:
                    category=category.find_all('li')
                    if category:
                        category=category[1].text
                        print(category)

            
            # time
            time=soup.find('span',class_='tts_time published_time')
            if time:
                print(time.get('content'))
                



            # content
            p=div.find_all('p')
            content=str()
            if p:
                for x in p:
                    content+=x.text
                print(content)



            if tag:
                tag=tag.find_all('strong')
                tags=str()
                for x in tag:
                    tags+=x.text
                    if x!=tag[-1]:
                        tags+=', '
                print(tags)

else:
    print('Failed to retrieve the web page. Status code:', response.status_code)



