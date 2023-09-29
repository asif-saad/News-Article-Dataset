import requests
from bs4 import BeautifulSoup


url='https://ekattor.tv/politics/'
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

        

        with open('output.txt', 'a', encoding='utf-8') as file:
            title=soup.find('div',class_='tag_title_holder')
            title=title.find('h1').text
            file.write(str(cnt)+'\t'+title)

        # div=soup.find_all('div',class_='tab_warp')
        # for x in div:
        #     x=x.find('a')
        #     print(x.get('href'))
                    


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    cnt+=1
    print(cnt,len(final))


