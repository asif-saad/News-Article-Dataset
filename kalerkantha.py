#text-left black--text text-h5 text-sm-h4 text-md-h3 mb-0 mb-sm-3


import requests
from bs4 import BeautifulSoup


cnt=0
url='https://www.kalerkantho.com/online/Politics/2023/09/27/1321849'
final=[url]

while cnt<1000:
    response = requests.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        links=soup.find_all('div',class_='card border-0')
        for link in links:
            x=link.find('a')
            x=x.get('href')
            x='https://www.kalerkantho.com/'+x
            if x not in final:
                final.append(x)

        links=soup.find('ul',class_='list-group list-group-flush pt-4')
        if links:
            link=links.find_all('a')
            for x in link:
                x=x.get('href')
                x='https://www.kalerkantho.com/'+x
                if x not in final:
                    final.append(x)
        # article_titles = soup.find('h1',class_='fw-700 e-mb-16')

        
        # divs_with_class = soup.select('div.section')
        # for div in divs_with_class:
        #     links = div.find_all('h3',class_='title')
        #     for h3 in links:
        #         a=h3.find('a')
        #         href=a.get('href')
        #         print(href)   

        title=soup.find('h1',class_='my-3')
        if title:
            with open('output.txt','a',encoding='utf-8') as file:
                file.write(str(cnt)+'\t'+title.text+'\n\n')


        # with open('output.txt', 'a', encoding='utf-8') as file:
        #     for title in article_titles:
        #         file.write(title.text+'\n\n')
        #     file.write('\n\n')


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    cnt+=1
    if cnt==len(final):
        print("done")
        break
    url=final[cnt]
    print(cnt,len(final))
