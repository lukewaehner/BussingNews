from bs4 import BeautifulSoup
import requests

subtags = ['technology', 'real-estate',
           'lifestyle', 'economy', 'watchlist', 'markets']
for tag in subtags:
    url = f"https://www.foxbusiness.com/{tag}"
    response = requests.get(url, headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

    if response.status_code == 200:
        html = response.text
        print(f"Page retrieved successfully for {tag}")
    else:
        print(f"Failed to retrieve the page for {tag}")
        continue

    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find_all('article', class_='article')

    for article in articles:
        title_element = article.find('h3', class_='title')
        link_element = title_element.find('a') if title_element else None

        if link_element and link_element.has_attr('href'):
            title = ' '.join(title_element.get_text().split())
            href = link_element['href']

            if not href.startswith('http'):
                href = f"https://www.foxbusiness.com{href}"

            print(title)
            print(href)
            print('')
