from bs4 import BeautifulSoup
import requests
from .crawlersettings.returnsettings import returnsettings


def crawlcnbc(subtags):
    # URL to request
    return_data = []

    # Headers
    headers = returnsettings()

    # Load cookies from JSON file if needed

    for tag in subtags:
        url = f"https://www.cnbc.com/{tag}"
        # Send GET request with cookies and headers
        try:
            response = requests.get(url,  headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', class_='Card-title')
                for element in links:
                    if element.has_attr('href'):
                        return_data.append(
                            {"title": element.text.strip(),
                             "url": element['href'],
                             "source": "CNBC"})
            else:
                print(f"Failed to retrieve the page: {tag}")
        except requests.exceptions.RequestException as e:
            print(f'request failed for {url} with error {e}')

    return return_data
