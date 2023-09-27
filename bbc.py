# focusIndicatorDisplayInlineBlock bbc-154s5g9 e1ifqd8t0



import requests
from bs4 import BeautifulSoup


cnt=0
url='https://www.bbc.com/bengali/articles/c51wjkyj7jwo'
final=[url]

while cnt<3000:

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        title=soup.find('h1',class_='bbc-qa2lun e1p3vdyi0')
        if title:
            with open('output.txt', 'a', encoding='utf-8') as file:
                file.write(str(cnt)+"\t"+title.text+'\n\n')

         


        links=soup.find_all('a',class_='focusIndicatorDisplayInlineBlock bbc-154s5g9 e1ifqd8t0')
        if links:
            for link in links:
                href=link.get('href')
                href='https://www.bbc.com'+href
                if href not in final:
                    final.append(href)
                
        links=soup.find_all('a',class_='focusIndicatorDisplayTableCell bbc-hq7sa5')
        if links:
            for link in links:
                href=link.get('href')
                if href not in final:
                    final.append(href)
                
        links=soup.find_all('a',class_='focusIndicatorDisplayInlineBlock bbc-154s5g9 e1ifqd8t0')
        if links:
            for link in links:
                href=link.get('href')
                href='https://www.bbc.com'+href
                if href not in final:
                    final.append(href)
                
        links=soup.find_all('a',class_='bbc-cr4eaj e145786u3')
        if links:
            for link in links:
                href=link.get('href')
                if href not in final:
                    final.append(href)
                
    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    cnt+=1
    if(cnt==len(final)):
        break
    url=final[cnt]
    print(len(final))

