# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import json
# import re

# driver = webdriver.Chrome()

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)

# driver.get('https://www.reuters.com/')

# with open('./cookies/reuters.json', 'rt') as cookies_file:
#     cookies = json.load(cookies_file)

# for cookie in cookies:
#     driver.add_cookie(cookie)

# driver.get('https://www.reuters.com/')


# # elements = driver.find_elements("xpath", '//a[@data-testid="heading"]')
# elements = driver.find_elements(By.TAG_NAME, 'a')

# print(len(elements))

# for element in elements:
#     href = element.get_attribute('href')
#     title = element.get_attribute('title')
#     if href and title and re.match(r'https://www\.reuters\.com/.+/.+/.+[a-zA-Z]', href):
#         print("Title: ", title)
#         print("Href: ", href)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import re


def crawlreuters(subtags=None):
    # Initialize the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get('https://www.reuters.com/')

        # Load cookies from file
        with open('./cookies/reuters.json', 'rt') as cookies_file:
            cookies = json.load(cookies_file)
        for cookie in cookies:
            driver.add_cookie(cookie)

        # Refresh the page after adding cookies
        driver.get('https://www.reuters.com/')

        # Find all <a> tags on the page
        elements = driver.find_elements(By.TAG_NAME, 'a')
        articles = []  # List to hold the scraped data

        # Extract title and href attributes from each <a> element
        for element in elements:
            href = element.get_attribute('href')
            title = element.get_attribute('title')
            if href and title and re.match(r'https://www\.reuters\.com/.+/.+/.+[a-zA-Z]', href):
                articles.append(
                    {"title": title, "url": href, "source": "Reuters"})

        return articles
    finally:
        driver.quit()  # Ensure the driver is closed properly

# Usage example (uncomment to run):
# scraped_articles = scrape_reuters()
# for article in scraped_articles:
#     print(f"Title: {article['title']}, URL: {article['url']}")
