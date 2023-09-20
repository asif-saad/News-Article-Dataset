#text-left black--text text-h5 text-sm-h4 text-md-h3 mb-0 mb-sm-3


import requests
from bs4 import BeautifulSoup


cnt=0
url='https://ekattor.tv/politics/51429/%E0%A6%B0%E0%A6%BE%E0%A6%B7%E0%A7%8D%E0%A6%9F%E0%A7%8D%E0%A6%B0%E0%A6%AF%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0-%E0%A6%A8%E0%A6%BF%E0%A6%B0%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%A4%E0%A6%A8%E0%A7%87%E0%A6%B0-%E0%A6%95%E0%A6%BE%E0%A6%B0%E0%A6%96%E0%A6%BE%E0%A6%A8%E0%A6%BE'
final=[url]
while cnt<5000:

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
    url=final[cnt]
    print(len(final))

