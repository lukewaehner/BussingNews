import json
import requests
from bs4 import BeautifulSoup


def crawlbloomberg(subtags):
    articles_list = []

    # Load cookies from JSON file
    with open('/Users/lukewaehner/Repos/BussingNews/backend/crawlers/cookies/bloomberg.json', 'rt') as cookies_file:
        cookie_list = json.load(cookies_file)

    # Transform the list of cookie dictionaries into a single dictionary
    cookies = {cookie['name']: cookie['value']
               for cookie in cookie_list if 'name' in cookie and 'value' in cookie}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    for tag in subtags:
        url = f"https://www.bloomberg.com/{tag}"

        response = requests.get(url, headers=headers, cookies=cookies)

        if response.status_code != 200:
            print(f"Failed to retrieve the page for {tag}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        # Debugging: Save the response to a file
        with open("output.html", "w") as file:
            file.write(response.text)

        # Find all <a> tags where the href attribute starts with '/news/articles/'
        links = soup.find_all(
            'a', href=lambda href: href and href.startswith('/news/articles/'))
        for link in links:
            title = link.get_text(strip=True)
            href = link['href']
            # Ensure the URL is complete
            if not href.startswith('http'):
                href = f"https://www.bloomberg.com{href}"
            articles_list.append(
                {"title": title, "url": href, "source": "Bloomberg"})

    return articles_list


# Example usage
# subtags = ['markets', 'economics', 'industries',
#            'technology', 'ai', 'politics', 'wealth', 'crypto']
# articles = crawlbloomberg(subtags)
# print(articles)
