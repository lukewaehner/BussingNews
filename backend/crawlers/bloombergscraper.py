import requests
import json
import os

# constant
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}


urls = ['https://www.bloomberg.com/lineup-next/api/page/markets-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
        'https://www.bloomberg.com/lineup-next/api/page/markets-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
        'https://www.bloomberg.com/lineup-next/api/page/markets-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
        ]

# these dont work?
others = ['https://www.bloomberg.com/lineup-next/api/page/economics-v2/module/quicktake,new_economy_video?moduleVariations=4_up_images,default&moduleTypes=story_package,video&locale=en&publishedState=PUBLISHED',
          'https://www.bloomberg.com/lineup-next/api/page/industries-v2/module/video?moduleVariations=default&moduleTypes=video&locale=en&publishedState=PUBLISHED',
          'https://www.bloomberg.com/lineup-next/api/page/technology-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
          'https://www.bloomberg.com/lineup-next/api/page/technology-vp/module/hub_story_list,pagination_mobile_ad,hub_ad_3?moduleVariations=default,default,default&moduleTypes=story_list,ad,ad&locale=en&publishedState=PUBLISHED']

script_dir = os.path.dirname(os.path.abspath(__file__))


def markets(urls):
    # URL to request
    return_data = []
    cookies_json = os.path.join(script_dir, 'cookies/bloomberg_markets.json')
    with open(cookies_json, 'rt') as cookies_file:
        cookie_list = json.load(cookies_file)

    # Transform the list of cookie dictionaries into a single dictionary
    cookies = {cookie['name']: cookie['value']
               for cookie in cookie_list if 'name' in cookie and 'value' in cookie}

    for url in urls:
        # Send GET request with cookies and headers
        response = requests.get(url, cookies=cookies, headers=headers)

        if response.status_code != 200:
            print(response.status_code)
            print(f"Failed to retrieve the page for {url}")
            try:
                requests.get(url)
                print("Retrying without cookies")
                print(response.status_code)
            except Exception as e:
                print(e)
        else:
            data = response.json()
            for item in data['modules']['pagination_story_list']['items']:
                url = item['url']
                return_data.append(
                    {"title": item['headline'], "url": f"https://www.bloomberg.com{url}", "time": item['publishedAt'], "source": "Bloomberg"})
    return return_data


def economics(others):
    cookies_json = os.path.join(script_dir, 'cookies/bloomberg_economics.json')
    with open(cookies_json, 'rt') as cookies_file:
        cookie_list = json.load(cookies_file)


# Transform the list of cookie dictionaries into a single dictionary
    cookies = {cookie['name']: cookie['value']
               for cookie in cookie_list if 'name' in cookie and 'value' in cookie}

    for url in others:
        response = requests.get(url, cookies=cookies, headers=headers)

        if response.status_code != 200:
            print(response.status_code)
            print(f"Failed to retrieve the page for {url}")
            try:
                requests.get(url)
                print("Retrying without cookies")
                print(response.status_code)
            except Exception as e:
                print(e)
        else:
            data = response.json()
            for item in data['modules']['pagination_story_list']['items']:
                url = item['url']
                print(item['headline'])
                print(f"https://www.bloomberg.com{url}")
                print(item['publishedAt'])
                print()


def crawlbloomberg(tags=None, subtags=None):
    articles_list = []
    articles_list += markets(urls)
    return articles_list
