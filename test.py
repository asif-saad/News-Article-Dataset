from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup



# URL of the webpage
url = "https://www.prothomalo.com/politics/zubwkuof15"

# Initialize the Chrome WebDriver (you can choose a different browser if needed)
cnt=0
final=[url]



while cnt<50:

    driver = webdriver.Chrome()

    while True:
        # Open the webpage
        driver.get(url)
        # Wait for some time to let the page load (you may need to adjust the time)
        driver.implicitly_wait(5)



        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Find and extract the titles of articles
            title = soup.find('h1',class_='IiRps')

            with open('output.txt', 'a', encoding='utf-8') as file:
                if title:
                    file.write(str(cnt)+'\t'+title.text+'\n\n')


        else:
            print('Failed to retrieve the web page. Status code:', response.status_code)


        # Find all <a> tags with class="jIq8p"
        a_tags = driver.find_elements(By.CSS_SELECTOR, 'a.jIq8p')

        # Loop through and print all <a> tags
        for a_tag in a_tags:
            if a_tag.get_attribute('href') not in final:
                final.append(a_tag.get_attribute('href'))


        a_tags=driver.find_elements(By.CSS_SELECTOR, 'a.card-with-image-zoom')
        for a_tag in a_tags:
            if a_tag.get_attribute('href') not in final:
                final.append(a_tag.get_attribute('href'))

        cnt+=1
        url=final[cnt]
        print(cnt,len(final))
        
        if cnt%50<40:
            break

    # Close the WebDriver
    driver.quit()
