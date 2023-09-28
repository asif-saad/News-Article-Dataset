import requests
from bs4 import BeautifulSoup

url='https://dbcnews.tv/articles/%E0%A6%95%E0%A6%BF%E0%A6%9B%E0%A7%81-%E0%A6%97%E0%A7%8B%E0%A6%B7%E0%A7%8D%E0%A6%A0%E0%A7%80-%E0%A6%AF%E0%A7%81%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%B0%E0%A6%BE%E0%A6%B7%E0%A7%8D%E0%A6%9F%E0%A7%8D%E0%A6%B0%E0%A7%87%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%A4%E0%A6%BF%E0%A6%95%E0%A7%8D%E0%A6%A4%E0%A6%A4%E0%A6%BE-%E0%A6%B8%E0%A7%83%E0%A6%B7%E0%A7%8D%E0%A6%9F%E0%A6%BF%E0%A6%B0-%E0%A6%9A%E0%A7%87%E0%A6%B7%E0%A7%8D%E0%A6%9F%E0%A6%BE-%E0%A6%95%E0%A6%B0%E0%A6%9B%E0%A7%87-%E0%A6%AA%E0%A6%B0%E0%A6%B0%E0%A6%BE%E0%A6%B7%E0%A7%8D%E0%A6%9F%E0%A7%8D%E0%A6%B0%E0%A6%AE%E0%A6%A8%E0%A7%8D%E0%A6%A4%E0%A7%8D%E0%A6%B0%E0%A7%80'


response = requests.get(url)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    # links=soup.find('div',class_='grid grid-cols-12 gap-1 sm:gap-2 grid-rows-12')
    # if links:
    #     link=links.find_all('a')
    #     if link:
    #         for x in link:
    #             href=x.get('href')
    #             print(href+'\n')


    links=soup.find_all('a')
    # links=soup.find('div',class_='w-full md:w-8/12 lg:w-9/12')
    if links:
        link=links
        if link:
            for x in link:
                href=x.get('href')
                print(href)
                


    # with open('output.txt', 'a', encoding='utf-8') as file:
    #     for title in article_titles:
    #         file.write(title.text+'\n\n')
    #     file.write('\n\n')


else:
    print('Failed to retrieve the web page. Status code:', response.status_code)
