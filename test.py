import requests
from bs4 import BeautifulSoup
from datasets.dataset_dict import DatasetDict
from datasets import Dataset
import jsonlines

url="https://www.ittefaq.com.bd/306484/"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    content=soup.find('div',class_='viewport jw_article_body')
    if content:
        # contents=content.find_all('p')
        # if contents:
        #     for x in contents:
        #         print(x.text)
        for x in content:
            print(x.text)