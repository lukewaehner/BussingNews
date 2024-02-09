from bs4 import BeautifulSoup
import requests

subtags = ['markets', 'economy', 'finance', 'energy',
           'investing', 'tech', 'world/?region=world']

for tag in subtags:

    url = f"https://www.cnbc.com/{tag}"

    response = requests.get(url, headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

    if response.status_code == 200:
        html = response.text
        print("Page retrieved successfully")
    else:
        print("Failed to retrieve the page")

    soup = BeautifulSoup(html, 'html.parser')

    links = soup.find_all('a', class_='Card-title')
    for element in links:
        if element.has_attr('href'):
            print(element.text.strip())
            print(element['href'])
