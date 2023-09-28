from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.channel24bd.tv/countries/article/174884/%E0%A6%AC%E0%A6%BE%E0%A6%97%E0%A7%87%E0%A6%B0%E0%A6%B9%E0%A6%BE%E0%A6%9F%E0%A7%87-%E0%A6%A6%E0%A7%81%E0%A6%87-%E0%A6%AE%E0%A7%8B%E0%A6%9F%E0%A6%B0%E0%A6%B8%E0%A6%BE%E0%A6%87%E0%A6%95%E0%A7%87%E0%A6%B2%E0%A7%87%E0%A6%B0-%E0%A6%AE%E0%A7%81%E0%A6%96%E0%A7%8B%E0%A6%AE%E0%A7%81%E0%A6%96%E0%A6%BF-%E0%A6%B8%E0%A6%82%E0%A6%98%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A7%87-%E0%A6%A8%E0%A6%BF%E0%A6%B9%E0%A6%A4-%E0%A7%A8"

# Initialize the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get(url)

# Wait for some time to let the page load (you may need to adjust the time)
driver.implicitly_wait(10)

# Get the page source after it has fully loaded
page_source = driver.page_source

# Close the WebDriver
driver.quit()

# Parse the HTML content of the webpage
soup = BeautifulSoup(page_source, 'html.parser')

# Find all <a> tags
a_tags = soup.find_all('a')

# Loop through and print all <a> tags
for a_tag in a_tags:
    print(a_tag)
