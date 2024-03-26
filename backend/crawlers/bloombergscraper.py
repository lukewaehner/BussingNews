from .crawlersettings.returnsettings import returnsettings
import os
import json
import requests


# Assuming `returnsettings` is modified to easily rotate settings on retries
# and 'settings.py' is located appropriately within your project structure.


def crawlbloomberg(tags=None):
    # URL to request
    return_data = []

    # Headers
    headers = returnsettings()

    # Proxies
    urls = ['https://www.bloomberg.com/lineup-next/api/page/markets-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
            'https://www.bloomberg.com/lineup-next/api/page/markets-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
            'https://www.bloomberg.com/lineup-next/api/page/markets-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
            'https://www.bloomberg.com/lineup-next/api/page/economics-v2/module/quicktake,new_economy_video?moduleVariations=4_up_images,default&moduleTypes=story_package,video&locale=en&publishedState=PUBLISHED',
            'https://www.bloomberg.com/lineup-next/api/page/industries-v2/module/video?moduleVariations=default&moduleTypes=video&locale=en&publishedState=PUBLISHED',
            'https://www.bloomberg.com/lineup-next/api/page/technology-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
            'https://www.bloomberg.com/lineup-next/api/page/technology-vp/module/hub_story_list,pagination_mobile_ad,hub_ad_3?moduleVariations=default,default,default&moduleTypes=story_list,ad,ad&locale=en&publishedState=PUBLISHED']

    # Load cookies from JSON file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cookies_json = os.path.join(script_dir, 'cookies/bloomberg_markets.json')
    with open(cookies_json, 'rt') as cookies_file:
        cookie_list = json.load(cookies_file)

    # Transform the list of cookie dictionaries into a single dictionary
    cookies = {cookie['name']: cookie['value']
               for cookie in cookie_list if 'name' in cookie and 'value' in cookie}

    for url in urls:
        # Send GET request with cookies and headers
        try:
            response = requests.get(
                url, cookies=cookies, headers=headers)

            if response.status_code == 200:
                data = response.json()
                print(data)
                for item in data['modules']['pagination_story_list']['items']:
                    url = item['url']
                    return_data.append(
                        {"title": item['headline'], "url": f"https://www.bloomberg.com{url}", "time": item['publishedAt'], "source": "Bloomberg"
                         })
            else:
                print(
                    f"Failed to retrieve the page for {url} with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f'request failed for {url} with error {e}')

    return return_data
