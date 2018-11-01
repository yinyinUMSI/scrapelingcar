#################################
'''
            ******* CHALLENGE #1 ********
    Polling in Real Time: The 2018 Midterm Elections

Task: Scrape the statistics for the midterms that NYT is currently tracking

0. Set up a cache
1. Get the number of calls made so far
2. Create a list called `current_races`
3. For each race that the NYT is currently tracking save the following in a list:
    1. type string :: Race id
    2. type string :: Race location
    3. type string :: Race summary
    4. type string :: Democratic candidate name
    5. type string :: percent democratic candidate
    6. type string :: Republicam candidate name
    7. type string :: percent republican candidate
    8. type string :: Undecided candidate name
    9. type string :: percent undecided
4. For each list representing (2), append to the `current_races` list
5. Print the following for each element in `current_race`:
    """ DEM:{} {} :: REP: {} {} :: UNDECIDED: {}""".format(
        "democratic candidate", "percent democrat",
        "republican candidate", "percent republican",
        "percent undecided"
    ))
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
    return "{}_{}_{}.json".format(site, topic, str(datetime.now()).replace(' ', ''))

def process(response):
    ## use the `response` to create a BeautifulSoup object
    soup = BeautifulSoup(response, 'html.parser')
    body = soup.find("div", class_ = "index-call-count svelte-dujgqx")
    print(body)
    #print(body)
    #div = section.find("span", class_ = "svelte-8g91sv")
    #numberlst = body.find_all("span", class_ = "char svelte-axwlyu")
    #print(numberlst)
    #print(numberlst)


###################
#     CONFIG      #
###################
cache_file = "nyt_class.json"
site="nyt"
topic="nyt_election"
cache = Cache(cache_file)
base = "https://www.nytimes.com/interactive/2018/upshot/elections-polls.html?action=click&module=Spotlight&pgtype=Homepage"


#######################
#     RUN PROGRAM     #
#######################
UID = create_id(site, topic)
response = cache.get(UID)

if response == None:
    response = requests.get(base).text
    cache.set(UID, response, 1)

process(response)
