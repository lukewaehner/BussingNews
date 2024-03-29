from bs4 import BeautifulSoup
import requests
from .crawlersettings.returnsettings import returnsettings
from datetime import datetime, timedelta
import re


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
                articles = soup.find_all('div', class_='Card-titleAndFooter')
                for article in articles:
                    title_element = article.find('a', class_='Card-title')
                    time_element = article.find('span', class_='Card-time')
                    rettime = None  # Initialize rettime
                    if time_element and time_element.get_text() is not None:
                        str_time = time_element.get_text()
                        if 'hours ago' in str_time:
                            time_curr = datetime.now()
                            time_sub = timedelta(
                                hours=(int(re.search(r'\d+', str_time).group())))
                            rettime = time_curr - time_sub
                        elif time_element and 'hours ago' not in time_element.get_text():
                            try:
                                rettime = datetime.strptime(
                                    str_time, "%a, %b %dth %Y")
                                rettime = rettime.replace(
                                    year=datetime.now().year)
                            except ValueError:
                                try:
                                    rettime = datetime.strptime(
                                        str_time, "%a , %b %dth %y")
                                except ValueError:
                                    rettime = datetime.now()
                        else:
                            rettime = datetime.now()
                    return_data.append(
                        {"title": title_element.text.strip(),
                            "url": title_element['href'],
                            "date":  rettime,
                            "source": "CNBC"})
            else:
                print(f"Failed to retrieve the page: {tag}")

        except requests.exceptions.RequestException as e:
            print(f'request failed for {url} with error {e}')

    return return_data
