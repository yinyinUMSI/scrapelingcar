#################################
'''
            ******* (super) CHALLENGE #2 ********
               'JOB OPENINGS @ New York Times'

Task: Scrape the NYT jobs page

0. Set up a cache
1. Create a list called `jobs`
2. For job save the following in a list:
    1. type string :: Job title
    2. type string :: Location
    3. type string :: Time posted
    4. type string :: Democratic candidate name
    5. type string :: URL
3. For each list representing (2), append to the `jobs` list
3. Save the output as a json

*****
You will run into so problems when trying to complete this challenge! Why? What
could you do to get the data that you want?
'''
#################################

from bs4 import BeautifulSoup
from alternate_advanced_caching import Cache
import requests
from datetime import datetime

##############
# SETTING UP #
##############


def create_id(site, topic):
    return "{}_{}_{}.json".format(site, topic, str(datetime.datetime.now()).replace(' ', ''))

def process(response):
    ## use the `response` to create a BeautifulSoup object
    soup = BeautifulSoup( <something here>, 'html.parser')

    ## DO STUFF:


###################
#     CONFIG      #
###################
cache_file = ""
site=""
topic=""
cache = Cache(cache_file)
base = "https://nytimes.wd5.myworkdayjobs.com/Tech"


#######################
#     RUN PROGRAM     #
#######################

if response == None:
    response = requests.get(base).text
    cache.set(UID, response, 1)

process(response)
