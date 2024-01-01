import requests
from bs4 import BeautifulSoup


url='https://www.dhakapost.com/international/249521'
# Send an HTTP request to the specified URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information based on the HTML structure of the website
    # For example, if news articles are in <div> elements with class "article"
    title=soup.find('h1',class_='text-[color:var(--link-color)] text-3xl lg:text-4xl leading-[40px] lg:leading-[50px] mb-6 dark:text-white print:dark:text-black print:text-2xl print:mb-2')
    content=soup.find('div',class_='news-details text-[color:var(--link-color)] mt-3 [font-size:var(--details-font)] leading-8 print:leading-7 dark:text-white break-words print:dark:text-black print:text-base')
    if content:
        print(content.find_all())

    if title:
        print(title.text)

    
    


else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


