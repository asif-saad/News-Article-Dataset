import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the website you want to scrape
# url = 'https://www.prothomalo.com/business/xj27ffhs63'
# url='https://www.prothomalo.com/business/kh9mpicu8e'
# url='https://www.prothomalo.com/world/ivhplp1kyc'
# url='https://www.prothomalo.com/bangladesh/district/ap9lkez94i'
# url='https://www.prothomalo.com/world/ivhplp1kyc'
url='https://www.prothomalo.com/world/europe/s2x8s9k7o0'


# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract the titles of articles
    article_titles = soup.find('h1',class_='IiRps')





    content_div=soup.find('div',class_='story-content no-key-elements')
    if content_div:
        p_tags=content_div.find_all('p')




    time = soup.find('div', class_='xuoYp')
    if time:
        # Find the <span> tag within the "xuoYp" <div>
        time = time.find('span')
        # Get the text inside the <span> tag
        time = time.text





    with open('output.txt', 'a', encoding='utf-8') as file:
        
        for title in article_titles:
            file.write(title.text+'\n\n')


        file.write(time+'\n\n')


        for tag in p_tags:
            text=tag.get_text()
            tag.string=text
            file.write(tag.decode_contents()+'\n')
        file.write('\n\n\n\n\n')


else:
    print('Failed to retrieve the web page. Status code:', response.status_code)
