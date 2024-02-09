from bs4 import BeautifulSoup
import requests

subtags = ['markets', 'economics', 'industries', 'technology', 'ai', 'politics', 'wealth', 'crypto']
for tag in subtags:
    url = f"https://www.bloomberg.com/{tag}"
    response = requests.get(url, headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
    
    if response.status_code == 200:
        html = response.text
        print(f"Page retrieved successfully for {tag}")
    else:
        print(f"Failed to retrieve the page for {tag}")
        continue

    soup = BeautifulSoup(html, 'html.parser')

    # Assuming that 'data-component' is a common attribute for article elements
    # and 'headline' is a sub-class or another attribute for titles
    articles = soup.find_all("title")
    print(articles)

    for article in articles:
        # Find the 'a' element directly since it seems to contain the href and the text based on the screenshot
        link_element = article.find('a')

        if link_element and link_element.has_attr('href'):
            title = ''.join(link_element.get_text().split())
            href = link_element['href']
            
            # Correcting the URL if it's a relative link
            if not href.startswith('http'):
                href = f"https://www.bloomberg.com{href}"
            
            print(title)
            print(href)
            print('')
