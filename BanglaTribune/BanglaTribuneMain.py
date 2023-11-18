import requests
from bs4 import BeautifulSoup


url="https://www.banglatribune.com/258267"
response=requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    header=soup.find('h1',class_='title mb10')
    time=soup.find('span',class_='tts_time')
    content=soup.find('div',class_='viewport jw_article_body')
    category=soup.find('div',class_='breadcrumb')
    category=category.find('ul').find_all('li')
    print(header.text)
    print(time.text)
    # content=content.find_all('p')
    # for i in content:
    #     print(i.text)

    print(category[1].find('strong',itemprop='name').text)
