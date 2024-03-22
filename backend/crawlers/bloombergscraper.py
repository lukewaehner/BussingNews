# from bs4 import BeautifulSoup
# import requests

# subtags = ['markets', 'economics', 'industries', 'technology', 'ai', 'politics', 'wealth', 'crypto']
# for tag in subtags:
#     url = f"https://www.bloomberg.com/{tag}"
#     response = requests.get(url, headers={
#         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

#     if response.status_code == 200:
#         html = response.text
#         print(f"Page retrieved successfully for {tag}")
#     else:
#         print(f"Failed to retrieve the page for {tag}")
#         continue

#     soup = BeautifulSoup(html, 'html.parser')

#     articles = soup.find_all("title")
#     print(articles)

#     for article in articles:
#         link_element = article.find('a')

#         if link_element and link_element.has_attr('href'):
#             title = ''.join(link_element.get_text().split())
#             href = link_element['href']

#             if not href.startswith('http'):
#                 href = f"https://www.bloomberg.com{href}"

#             print(title)
#             print(href)
#             print('')

# bloomberg_scraper.py
from bs4 import BeautifulSoup
import requests


def crawlbloomberg(subtags):
    articles_list = []
    for tag in subtags:
        url = f"https://www.bloomberg.com/{tag}"
        response = requests.get(url, headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

        if response.status_code != 200:
            print(f"Failed to retrieve the page for {tag}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all divs with `data-type` attribute set to "article"
        article_divs = soup.find_all("div", attrs={"data-type": "article"})

        for div in article_divs:
            # Within each article div, find the headline div
            headline_div = div.find(
                "div", attrs={"data-component": "headline"})
            if headline_div:
                link_element = headline_div.find('a', href=True)
                # Check if the link element exists and has a non-empty href attribute
                if link_element and link_element['href']:
                    title = link_element.get_text(strip=True)
                    href = link_element['href']
                    # Ensure the URL is complete
                    if not href.startswith('http'):
                        href = f"https://www.bloomberg.com{href}"
                    articles_list.append(
                        {"title": title, "url": href, "source": "Bloomberg"})

    return articles_list
