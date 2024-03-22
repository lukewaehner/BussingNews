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
        "function": crawlreuters,  # this one is broken
        "subtags": []  # No subtags for Reuters yet
    },
    {
        "function": crawlwsj,
        "subtags": ['world', 'us', 'politics', 'economy', 'business', 'markets']
    }
]


def job():
    for crawler in crawlerlist:
        crawler_function = crawler["function"]
        subtags = crawler["subtags"]
        articles = crawler_function(subtags)
        if articles:
            # Insert articles into the database
            # insert_articles(articles)
            print(articles[0])  # For testing, print the first article
        else:
            print("No articles fetched for this scraper.")


job()
# schedule.every(10).minutes.do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
