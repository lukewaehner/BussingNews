import requests
from .crawlersettings.returnsettings import returnsettings

tags = ['world', 'business', 'markets', 'sustainability',
        'legal',  'technology', 'breakingviews']


def crawlreuters(tags, subtags=None):
    return_data = []
    size = 100  # Set the size for fetching articles
    headers = returnsettings()
    for tag in tags:
        try:
            REUTERS_URI = f'https://www.reuters.com/pf/api/v3/content/fetch/recent-stories-by-sections-v1?query=%7B%22section_ids%22%3A%22%2F{tag}%2F%22%2C%22size%22%3A{size}%2C%22website%22%3A%22reuters%22%7D&d=183&_website=reuters'

            response = requests.get(REUTERS_URI, headers=headers)

            if response.status_code == 200:
                data = response.json()
                if not data['result']['articles']:
                    print(f"No articles found for {tag}")
                    continue

                for item in data['result']['articles']:
                    headline = item['title']
                    url = item['canonical_url']
                    time = item['published_time']
                    return_data.append(
                        {"title": headline, "url": url, "time": time, "source": "Reuters"})

            else:
                print(f"Failed to retrieve the page for {tag}")

        except requests.exceptions.RequestException as e:
            print(f'request failed for {tag} with error {e}')
    return return_data
