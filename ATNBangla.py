#pop-inside-3 pop-inside


import requests
from bs4 import BeautifulSoup


cnt=0
url='https://www.atnbangla.tv/%e0%a6%86%e0%a6%9c-%e0%a6%8f%e0%a6%95%e0%a7%81%e0%a6%b6%e0%a7%87-%e0%a6%aa%e0%a6%a6%e0%a6%95-%e0%a6%aa%e0%a7%8d%e0%a6%b0%e0%a6%a6%e0%a6%be%e0%a6%a8-%e0%a6%95%e0%a6%b0%e0%a6%ac%e0%a7%87%e0%a6%a8/'
final=[url]


while cnt<100:

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find('div',class_='pop-inside-3 pop-inside')
        title=soup.find('h1',class_='entry-title')
        link=links.find_all('a')
        for x in link:
            href=x.get('href')
            if href not in final:
                final.append(href)
            

        with open('output.txt', 'a', encoding='utf-8') as file:
            if title:
                file.write(str(cnt)+'\t'+title.text+'\n\n')


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    cnt+=1
    if cnt==len(final):
        break
    url=final[cnt]
    print(len(final))
