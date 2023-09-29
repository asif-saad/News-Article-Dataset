import requests
from bs4 import BeautifulSoup


cnt=0
url='https://www.prothomalo.com/sports/cricket/g90ejvyrim'
final=[url]

while cnt<50:
    print(cnt)
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        a=soup.find_all('a',target="_blank")
        if a:
            for x in a:
                tmp=x.get('href')
                if "https://www.prothomalo.com" in tmp and tmp not in final:
                    print(tmp)
                    final.append(tmp)
                    


    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)
    
    cnt+=1
    if cnt>=len(final):
        cnt=0
    url=final[cnt]
