from .crawlersettings.returnsettings import returnsettings
import os
import json
import requests
import re
from datetime import datetime

# Assuming `returnsettings` is modified to easily rotate settings on retries
# and 'settings.py' is located appropriately within your project structure.


def processData(item):
    url = item['url']
    time = item['publishedAt']
    datetime_obj = datetime.strptime(
        time, "%Y-%m-%dT%H:%M:%S.%fZ")
    return {"title": item['headline'], "url": f"https://www.bloomberg.com{url}", "date": datetime_obj, "source": "Bloomberg"}


def crawlbloomberg(tags=None):
    return_data = []

    # Headers
    headers = returnsettings()

    # URLs to reuqest from
    urls = ['https://www.bloomberg.com/lineup-next/api/page/markets-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
            'https://www.bloomberg.com/lineup-next/api/page/economics-v2/module/quicktake,new_economy_video?moduleVariations=4_up_images,default&moduleTypes=story_package,video&locale=en&publishedState=PUBLISHED',
            'https://www.bloomberg.com/lineup-next/api/page/technology-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
            'https://www.bloomberg.com/lineup-next/api/page/technology-vp/module/hub_story_list,pagination_mobile_ad,hub_ad_3?moduleVariations=default,default,default&moduleTypes=story_list,ad,ad&locale=en&publishedState=PUBLISHED'
            ]

    # Load cookies from JSON file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cookies_json = os.path.join(script_dir, 'cookies/bloomberg_markets.json')
    with open(cookies_json, 'rt') as cookies_file:
        cookie_list = json.load(cookies_file)

    # Transform the list of cookie dictionaries into a single dictionary
    cookies = {cookie['name']: cookie['value']
               for cookie in cookie_list if 'name' in cookie and 'value' in cookie}

    altheader = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    for url in urls:
        pattern = r"/api/page/[^/]+/module/([^,?]+)"
        # Send GET request with cookies and headers
        try:
            response = requests.get(
                url, headers=altheader)

            if response.status_code == 200:
                data = response.json()
                # normal method
                try:
                    # grab the iterable key
                    first_key = list(data.keys())[0]
                    for item in data[first_key]['items']:
                        # process the data with predefined schema, this doesn't seem to change
                        return_data.append(processData(item))

                # except any error
                except Exception as e:
                    print(f'error for {url} with error {e}')
                    # nest this try statement I cant remember where this even comes from haha
                    try:
                        match = re.search(pattern, url)
                        array_articles = str(match.group(1))
                        for item in data['modules'][array_articles]['items']:
                            url = item['url']
                            time = item['publishedAt']
                            datetime_obj = datetime.strptime(
                                time, "%Y-%m-%dT%H:%M:%S.%fZ")
                            return_data.append(
                                {"title": item['headline'], "url": f"https://www.bloomberg.com{url}", "date": datetime_obj, "source": "Bloomberg"
                                 })
                    # except keyerror
                    except KeyError as e:
                        print(f'keyerror for {url} with error {e}')

            else:
                print(
                    f"Failed to retrieve the page for {url} with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f'request failed for {url} with error {e}')
    return return_data
