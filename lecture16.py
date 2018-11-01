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
cache_file = "linger.json"
site="lingcar"
topic="dive"
cache = Cache(cache_file)
base = "https://www.lingscars.com/"


#######################
#     RUN PROGRAM     #
#######################
UID = create_id(site, topic)
response = cache.get(UID)

if response == None:
    response = requests.get(base).text
    cache.set(UID, response, 1)

process(response)
