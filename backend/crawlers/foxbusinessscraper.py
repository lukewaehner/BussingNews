# to add date -> <article> <time datetime="XXXXXX">
# need to get the dateimte=XXXXX from the article

from bs4 import BeautifulSoup
import requests


def crawlfoxbusiness(subtags):
    articles_list = []
    for tag in subtags:
        url = f"https://www.foxbusiness.com/{tag}"
        response = requests.get(url, headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

        if response.status_code != 200:
            print(f"Failed to retrieve the page for {tag}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='article')

        for article in articles:
            title_element = article.find('h3', class_='title')
            link_element = title_element.find('a') if title_element else None
            if link_element and link_element.has_attr('href'):
                title = ' '.join(title_element.get_text().split())
                href = link_element['href']
                if not href.startswith('http'):
                    href = f"https://www.foxbusiness.com{href}"
                articles_list.append(
                    {"title": title, "url": href, "source": "Fox Business"})

    return articles_list
