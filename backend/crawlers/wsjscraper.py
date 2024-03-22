# from bs4 import BeautifulSoup
# import requests


# subtags = ['world', 'us', 'politics', 'economy', 'business',
#            'markets']
# for tag in subtags:
#     url = f"https://www.wsj.com/{tag}?mod=nav_top_section"
#     response = requests.get(url, headers={
#         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

#     if response.status_code == 200:
#         html = response.text
#         print("Page retrieved successfully")
#     else:
#         print("Failed to retrieve the page")

#     soup = BeautifulSoup(html, 'html.parser')

#     def linksSearch(tag):
#         conditions = ['HeadlineLink', 'HeadlineTextBlock']
#         if tag.has_attr('class'):
#             class_str = " ".join(tag['class'])
#             for condition in conditions:
#                 if condition in class_str:
#                     return True
#         return False

#     links = soup.find_all(linksSearch)
#     for element in links:
#         if element.has_attr('href'):
#             print(element.text.strip())
#             print(element['href'])

from bs4 import BeautifulSoup
import requests


def crawlwsj(subtags):
    articles_list = []  # List to hold the scraped data

    for tag in subtags:
        url = f"https://www.wsj.com/{tag}?mod=nav_top_section"
        response = requests.get(url, headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

        if response.status_code != 200:
            print(f"Failed to retrieve the page for {tag}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

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

    return articles_list

# Example usage:
# subtags = ['world', 'us', 'politics', 'economy', 'business', 'markets']
# articles = scrape_wsj(subtags)
# for article in articles:
#     print(f"Title: {article['title']}, URL: {article['url']}")
