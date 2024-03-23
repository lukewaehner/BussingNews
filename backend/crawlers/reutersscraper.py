from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import re
import time
import random


def crawlreuters(subtags=None):
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get('https://www.reuters.com/')
        time.sleep(random.uniform(2, 5))

        with open('./crawlers/cookies/reuters.json', 'rt') as cookies_file:
            cookies = json.load(cookies_file)
        for cookie in cookies:
            if "sameSite" in cookie and cookie["sameSite"] not in ["Strict", "Lax", "None"]:
                cookie["sameSite"] = "Lax"
            driver.add_cookie(cookie)
            time.sleep(random.uniform(0.5, 1))  # Adjust as necessary

        driver.get('https://www.reuters.com/')
        time.sleep(random.uniform(2, 5))

        # Locate article <header> tags containing <a> tags
        article_headers = driver.find_elements(By.CSS_SELECTOR, 'header a')
        articles = []

        for header in article_headers:
            # Attempt to find the first <span> within the <a> which might contain the title
            try:
                title_element = header.find_element(By.CSS_SELECTOR, 'span')
                title = title_element.text  # Assuming the title is the text of the first <span>
            except:
                title = ""  # If no <span> is found, or it doesn't contain the title

            href = header.get_attribute('href')
            if href and title:
                articles.append(
                    {"title": title, "url": href, "source": "Reuters"})
            # Be cautious with sleep in loops
            time.sleep(random.uniform(0.1, 0.3))

        return articles
    finally:
        driver.quit()
