import requests
from bs4 import BeautifulSoup
from datasets.dataset_dict import DatasetDict
from datasets import Dataset
import jsonlines




# cnt=703134
# url='https://www.bhorerkagoj.com/country/'
# response = requests.get(url+str(cnt))
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     title=soup.find('h1',class_='desktopDetailHeadline marginT0')
#     content=soup.find('div',class_='desktopDetailBody').find('div')
#     category=soup.find('p',class_='desktopDetailCat marginB15 hidden-print').find('strong')
#     time=soup.find('p',class_='desktopDetailPTime color1')
#     key=soup.find('div',class_='desktopDetailTag hidden-print')


#     if title:
#         title=title.find('strong')
#         print(title.text)
    
#     if content:
#         content=content.find_all('p')
#         # for x in content:
#         #     print(x.text)


#     print(category.text)
#     print(time.text)

#     if key:
#         key=key.find_all('a')
#         for x in key:
#             print(x.text)









titleFinal=str()
categoryFinal=str()
timeFinal=str()
contentFinal=str()
keyFinal=str()
outputText='Bhorerkagoj/output.txt'
lastvalText='Bhorerkagoj/last_val.txt'
jsonl='C:/Users/asifs/OneDrive/Desktop/dataset/Bhorerkagoj.jsonl'
d={'Bhorerkagoj':Dataset.from_dict({'Title':titleFinal,'Category':categoryFinal,
                                           'Time':timeFinal,'Content':contentFinal,
                                           'Key':keyFinal})}
raw_datasets=DatasetDict(d)
with open(lastvalText,'r') as file:
    cnt=int(file.read())

while True:
    print(cnt)
    url='https://www.bhorerkagoj.com/country/'+str(cnt)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title=soup.find('h1',class_='desktopDetailHeadline marginT0')
        content=soup.find('div',class_='desktopDetailBody')
        category=soup.find('p',class_='desktopDetailCat marginB15 hidden-print').find('strong')
        time=soup.find('p',class_='desktopDetailPTime color1')
        key=soup.find('div',class_='desktopDetailTag hidden-print')



        if title and content.find('div'):
            with open(outputText,'a',encoding='utf-8') as file2:
                with jsonlines.open(jsonl, "a") as writer:
                    title=title.find('strong')
                    title=title.text
                    titleFinal=title
                    # take title
                    file2.write(str(cnt)+'\n'+titleFinal+'\n')





                    # news content
                    content=content.find('div')
                    contentFinal+=content.text.replace('\n','')

                    file2.write('content:'+contentFinal+'\n')




                    # time date
                    if time:
                        timeFinal=time.text
                    
                    file2.write(timeFinal+'\n')




                    # category
                    categoryFinal=category.text
                    file2.write(categoryFinal+'\n')   




                    # key
                    if key:
                        key=key.find_all('a')
                        for x in key:
                            keyFinal+=x.text
                            if x!=key[-1]:
                                keyFinal+=" ,"
                    
                    file2.write(keyFinal+'\n')   


                    file2.write('\n\n\n')
                    writer.write({'Title':titleFinal,'Category':categoryFinal,
                                'Time':timeFinal, 'Content':contentFinal,
                                'Key':keyFinal})
    cnt+=1
    with open(lastvalText,'w') as file1:
        file1.write(str(cnt))



