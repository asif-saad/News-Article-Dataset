import requests
from bs4 import BeautifulSoup
from datasets.dataset_dict import DatasetDict
from datasets import Dataset
import jsonlines
import re



url='https://www.ajkerpatrika.com/'+str(316279)
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title=soup.find('h1',class_='title')
    time=soup.find('span',class_='tts_time content_published_time')
    content=soup.find('div',class_='viewport jw_article_body')
    meta=soup.find('div',class_='content_highlights jw_detail_content_holder content mb16')
    category=soup.find('div',class_='breadcrumb')
    keyword=soup.find('div',class_='more_and_tag')
    print(title.text)
    print(time.text)
    print(content.text)
    if meta:
        if meta.find('p'):
            print(meta.find('p').text)
    
    if category:
        category=category.find_all('li')[1:]
        if category:
            for i in category:
                i=i.find('strong')
                print(i.text)

    if keyword:
        keyword=keyword.find_all('strong')
        for i in keyword:
            print(i.text)

