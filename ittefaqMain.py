import requests
from bs4 import BeautifulSoup
from datasets.dataset_dict import DatasetDict
from datasets import Dataset
import jsonlines
import http

titleFinal=str()
categoryFinal=str()
timeFinal=str()
contentFinal=str()
tagsFinal=str()
d={'EkattorTv':Dataset.from_dict({'Title':titleFinal,'Category':categoryFinal,'Time':timeFinal,'Content':contentFinal,'Tags':tagsFinal})}
raw_datasets=DatasetDict(d)

url1='https://www.ittefaq.com.bd/'
cnt=133044





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
            with open('output.txt','a',encoding='utf-8') as file:
                with jsonlines.open("C:/Users/asifs/OneDrive/Desktop/dataset/ittefaq.jsonl", "a") as writer:
                    titleFinal=str()
                    categoryFinal=str()
                    timeFinal=str()
                    contentFinal=str()
                    tagsFinal=str()





                    # titles
                    h1=h1.text
                    titleFinal=h1
                    file.write(str(cnt-15817)+','+str(cnt)+'\n'+titleFinal+'\n')




                    # category
                    if category:
                        category=category.find('span')
                        # print(category.text)
                        if category:
                            categoryFinal=category.text
                            file.write(categoryFinal+'\n')



                    # time
                    if date:
                        date=date.find('span',class_='tts_time')
                        # print(date.text)
                        if date:
                            timeFinal=date.text
                            file.write(timeFinal +'\n')





                    # contents
                    contentsx=contents.find_all('span')
                    if contentsx:
                        content=str()
                        for x in contentsx:
                            content+=x.text
                        # print(content)
                        contentFinal=content
                        file.write(contentFinal+'\n')
                    else:
                        contents=contents.find_all('p')
                        if contents:
                            content=str()
                            for x in contents:
                                content+=x.text
                            contentFinal=content
                            file.write(contentFinal+'\n')




                    # tags
                    if tags:
                        tags=tags.find_all('strong')
                        if tags:
                            tag=str()
                            for x in tags:
                                tag+=x.text
                                if x!=tag[-1]:
                                    tag+=', '
                            
                            # print(tag)
                            tagsFinal=tag
                            file.write('tags:'+tagsFinal)


                    file.write('\n\n\n')
                    writer.write({'Title':titleFinal,'Category':categoryFinal,'Time':timeFinal,
                                'Content':contentFinal,'Tags':tagsFinal})

                            


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
        
    

    # if cnt%300==0:
    #     import time
    #     time.sleep(70)

    cnt+=1

