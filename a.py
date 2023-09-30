import requests
from bs4 import BeautifulSoup



url='https://www.prothomalo.com'


# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    a=soup.find_all('a')
    if a:
        for x in a:
            print(x)
            print(x.get('href'))
            print('\n\n')


        # for x in a:
        #     tmp=x.get('href')
        #     if "https://www.prothomalo.com" in tmp and tmp not in final:
        #         print(tmp)
        #         final.append(tmp)
                


else:
    print('Failed to retrieve the web page. Status code:', response.status_code)


