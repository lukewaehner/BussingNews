import schedule
import time
# Adjust this import statement as necessary
from crawlers import crawlcnbc, crawlfoxbusiness, crawlbloomberg, crawlreuters, crawlwsj
# Adjust this import statement as necessary
from database import insertarticles

crawlerlist = [
    {
        "function": crawlcnbc,
        "subtags": ['markets', 'economy', 'finance', 'energy', 'investing', 'tech', 'world/?region=world']
    },
    {
        "function": crawlfoxbusiness,
        "subtags": ['technology', 'real-estate', 'lifestyle', 'economy', 'watchlist', 'markets']
    },
    {
        "function": crawlbloomberg,
        "subtags": ['markets', 'economics', 'industries', 'technology', 'ai', 'politics', 'wealth', 'crypto']
    },
    {
        "function": crawlreuters,
        "subtags": ['world', 'business', 'markets', 'sustainability',
                    'legal',  'technology', 'breakingviews']
    },

    {
        "function": crawlwsj,
        "subtags": ['world', 'us-news', 'politics', 'economy', 'business', 'tech', 'real-estate', 'finance'],
    }
]


def job():
    print("Running the scrapers")
    for crawler in crawlerlist:
        crawler_function = crawler["function"]
        subtags = crawler["subtags"]
        articles = crawler_function(subtags)

        # now process

        if articles:
            # Insert articles into the database
            insertarticles(articles)
        else:
            print(f'No articles fetched for this scraper, {crawler}.')


def test():
    print("Testing the scrapers")
    for crawler in crawlerlist:
        crawler_function = crawler["function"]
        subtags = crawler["subtags"]
        if ("alttags" in crawler):
            alttags = crawler["alttags"]
            articles = crawler_function(subtags, alttags)
        else:
            articles = crawler_function(subtags)

        # now process

        if articles:
            print(articles[0])  # For testing, print the first article
        else:
            print(f'No articles fetched for this scraper, {crawler}.')


print("Would you like to [t]est, or [r]un the job?")
response = input()
if response == 't':
    test()
elif response == 'r':
    job()
# schedule.every(10).minutes.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
