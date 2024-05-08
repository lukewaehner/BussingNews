from bs4 import BeautifulSoup
import requests
from .crawlersettings.returnsettings import returnsettings
import os
import json


def crawlwsj(subtags):
    articles_list = []  # List to hold the scraped data

    headers = returnsettings()

    # cookies processing
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cookies_json = os.path.join(script_dir, 'cookies/wsj.json')
    with open(cookies_json, 'rt') as cookies_file:
        cookie_list = json.load(cookies_file)

    cookies = {cookie['name']: cookie['value']
               for cookie in cookie_list if 'name' in cookie and 'value' in cookie}

    for tag in subtags:
        try:
            url = f"https://www.wsj.com/{tag}?mod=nav_top_section"
            response = requests.get(url, headers=headers, cookies=cookies)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
            else:
                print(
                    f"Failed to retrieve the page for {tag} with status code {response.status_code}")
                continue

            def links_search(tag):
                conditions = ['HeadlineLink', 'HeadlineTextBlock']
                if tag.has_attr('class'):
                    class_str = " ".join(tag['class'])
                    for condition in conditions:
                        if condition in class_str:
                            return True
                return False

            links = soup.find_all(links_search)
            for element in links:
                href = element.get('href', '')
                title = element.text.strip()
                if href:
                    articles_list.append(
                        {"title": title, "url": href, "source": "WSJ"})
        except requests.exceptions.RequestException as e:
            print(f'request failed for {tag} with error {e}')
    return articles_list


# Example usage:
# subtags = ['world', 'us', 'politics', 'economy', 'business', 'markets']
# articles = crawlwsj(subtags)
# for article in articles:
#     print(f"Title: {article['title']}, URL: {article['url']}")
