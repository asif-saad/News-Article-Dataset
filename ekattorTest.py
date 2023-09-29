import requests
from bs4 import BeautifulSoup


url='https://ekattor.tv/sports/35865/%E0%A6%95%E0%A6%BE%E0%A6%A4%E0%A6%BE%E0%A6%B0%E0%A7%87-%E0%A6%AA%E0%A7%8B%E0%A6%B6%E0%A6%BE%E0%A6%95%E0%A7%87%E0%A6%B0-%E0%A6%95%E0%A6%BE%E0%A6%B0%E0%A6%A3%E0%A7%87-%E0%A6%86%E0%A6%B2%E0%A7%8B%E0%A6%9A%E0%A6%BF%E0%A6%A4-%E0%A6%95%E0%A7%8D%E0%A6%B0%E0%A7%8B%E0%A7%9F%E0%A6%BE%E0%A6%9F-%E0%A6%AE%E0%A6%A1%E0%A7%87%E0%A6%B2'
cnt=0
final=[url]


while cnt<800:


    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        a=soup.find_all('a',class_="link_overlay")
        if a:
            for x in a:
                x='https:'+x.get('href')
                if x not in final:
                    final.append(x)

        

        with open('output1.txt', 'a', encoding='utf-8') as file:

            title=soup.find('h1',class_='title')
            if title:

                file.write(title.text+'\n\n')

                    


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    cnt+=1
    if cnt<len(final):
        url=final[cnt]
    else:
        break
    print(cnt,len(final),round(cnt/len(final),3))


