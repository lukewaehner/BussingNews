import schedule
import time
# Adjust this import statement as necessary
from crawlers import crawlcnbc, crawlfoxbusiness, crawlbloomberg, crawlreuters, crawlwsj
# Adjust this import statement as necessary
from database import insertarticles

crawlerlist = [
    {
        "function": crawlcnbc,
        "tags": ['markets', 'economy', 'finance', 'energy', 'investing', 'tech', 'world/?region=world']
    },
    {
        "function": crawlfoxbusiness,
        "tags": ['technology', 'real-estate', 'lifestyle', 'economy', 'watchlist', 'markets']
    },
    {
        "function": crawlbloomberg,
        "tags": None
    },
    {
        "function": crawlreuters,
        "tags": ['world', 'business', 'markets', 'sustainability',
                 'legal',  'technology', 'breakingviews']
    },

    {
        "function": crawlwsj,
        "tags": ['world', 'us-news', 'politics', 'economy', 'business', 'tech', 'real-estate', 'finance'],
    }
]


def job():
    print("Running the scrapers")
    for crawler in crawlerlist:
        crawler_function = crawler["function"]
        tags = crawler["tags"]
        articles = crawler_function(tags)

        # now process

        if articles:
            # Insert articles into the database
            print(
                f'Fetched {len(articles)} articles for this scraper, {crawler}.')
            insertarticles(articles)
        else:
            print(f'No articles fetched for this scraper, {crawler}.')


job()

# schedule.every(10).minutes.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
