import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# Ensure you've installed PySocks for SOCKS proxy support: pip install PySocks


def is_proxy_working(proxy):
    test_url = 'https://www.google.com/'
    try:
        response = requests.get(test_url, proxies=proxy, timeout=20)
        if response.status_code == 200:
            return True
    except requests.RequestException as e:
        print(f"Proxy failed with error: {e}")
    return False


def format_proxy(ip, port, protocols):
    # This example only handles HTTP and SOCKS proxies
    if 'socks4' in protocols or 'socks5' in protocols:
        protocol = 'socks4' if 'socks4' in protocols else 'socks5'
    else:
        protocol = 'http'
    proxy_str = f"{protocol}://{ip}:{port}"
    return {"http": proxy_str, "https": proxy_str}


def get_proxies(max_working_proxies):
    print("Starting proxy check")
    proxies_to_check = []

    response = requests.get(
        'https://proxylist.geonode.com/api/proxy-list?protocols=http%2Chttps&limit=500&page=1&sort_by=lastChecked&sort_type=desc')
    data = response.json()

    for proxy in data['data']:
        formatted_proxy = format_proxy(
            proxy['ip'], proxy['port'], proxy['protocols'])
        proxies_to_check.append(formatted_proxy)
        if len(proxies_to_check) >= max_working_proxies:
            break  # Limit the number of proxies to check

    working_proxies = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(is_proxy_working, proxy)
                   for proxy in proxies_to_check]

        for future in as_completed(futures):
            is_working = future.result()
            if is_working:
                working_proxy = futures[future]
                print(f"Proxy is working, added to list: {working_proxy}")
                working_proxies.append(working_proxy)
                if len(working_proxies) >= max_working_proxies:
                    print("Reached the desired number of working proxies.")
                    break  # Stop if we've reached the desired number of working proxies

    return working_proxies


if __name__ == "__main__":
    max_working_proxies = 5
    working_proxies = get_proxies(max_working_proxies)
    print(f"Found {len(working_proxies)} working proxies.")
