import requests
from bs4 import BeautifulSoup


url='https://ekattor.tv/33823'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    

    with open('output.txt', 'a', encoding='utf-8') as file:

        title=soup.find('h1',class_='title')
        div=soup.find('div',class_='viewport jw_article_body')
        
        
        tag=soup.find('div',class_='topic_list')
        if tag:
            strong=tag.find_all('strong')
            for x in strong:
                print(x.text)

        if title and div:

            p=div.find_all('p')
            content=str()
            for x in p:
                content+=x.text


        




        category=soup.find('div',class_="breadcrumb")
        if category:
            category=category.find('ul')
            if category:
                category=category.find_all('li')
                if category:
                    category=category[1].text
                    print(category)
else:
    print('Failed to retrieve the web page. Status code:', response.status_code)



