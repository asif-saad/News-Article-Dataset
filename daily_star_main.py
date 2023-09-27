#text-left black--text text-h5 text-sm-h4 text-md-h3 mb-0 mb-sm-3


import requests
from bs4 import BeautifulSoup


cnt=0
url='https://bangla.thedailystar.net/news/asia/india/news-516151'
final=[url]
while cnt<1000:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find and extract the titles of articles
        article_titles = soup.find('h1',class_='fw-700 e-mb-16')
        # links=soup.find_all('a',class_='link_overlay')
        # if links:
        #     with open('links.txt','a') as file:
        #         for link in links:
        #             href=link.get('href')
        #             # file.write(href+'\n')
        #             href='https:'+href

        
        divs_with_class = soup.select('div.section')
        for div in divs_with_class:
            links = div.find_all('h3',class_='title')
            for h3 in links:
                a=h3.find('a')
                href='https://bangla.thedailystar.net'+a.get('href')
                if href not in final:
                    final.append(href)
                  

        
        # p_with_class=soup.find_all('div',class_='type-counter')
        # for p in p_with_class:
        #     links=div.find_all('a')
        #     for link in links:
        #         href=link.get('href')
        #         print(href)   


        with open('output.txt', 'a', encoding='utf-8') as file:
            for title in article_titles:
                file.write(str(cnt)+"\t"+title.text+'\n\n')
            file.write('\n\n')


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)

    cnt+=1
    url=final[cnt]
    print(len(final))
