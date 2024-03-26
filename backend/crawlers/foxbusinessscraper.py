# to add date -> <article> <time datetime="XXXXXX">
# need to get the dateimte=XXXXX from the article

from bs4 import BeautifulSoup
import requests
from .crawlersettings.returnsettings import returnsettings


def crawlfoxbusiness(subtags):
    # URL to request
    return_data = []

    # Headers
    headers = returnsettings()

    # Load cookies from JSON file if needed

    for tag in subtags:
        url = f'https://www.foxbusiness.com/{tag}'
        # Send GET request with cookies and headers
        try:
            response = requests.get(url,  headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                articles = soup.find_all('article', class_='article')
                for article in articles:
                    title_element = article.find('h3', class_='title')
                    link_element = title_element.find(
                        'a') if title_element else None
                    if link_element and link_element.has_attr('href'):
                        title = ' '.join(title_element.get_text().split())
                        href = link_element['href']
                        if not href.startswith('http'):
                            href = f"https://www.foxbusiness.com{href}"
                        return_data.append(
                            {"title": title, "url": href, "source": "Fox Business"})
            else:
                print(f"Failed to retrieve the page: {tag}")
        except requests.exceptions.RequestException as e:
            print(f'request failed for {url} with error {e}')

    return return_data
