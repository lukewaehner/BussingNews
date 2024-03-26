import requests
import json

# Make the API call
choice = input(
    'Are you sure you want to run this, it will overwrite the headers_data.json file? Y/N')
if choice.lower() != 'y':
    exit()
else:
    response = requests.get(
        url='https://headers.scrapeops.io/v1/browser-headers',
        params={
            'api_key': '32726df5-60dc-4932-9bd9-6e784cc2ae31',
            'num_results': '100'}
    )

    # Convert the response to JSON format
    data = response.json()

    # Save the data to a JSON file
    with open('headers_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # If you want to print out the saved data
    for item in data['result']:
        print(item)
        print()
