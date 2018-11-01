#################################
'''
            ******* GETTING STARTED ********

Task: Scrape the New York Times Opinion section on the home page

0. Set up a cache
1. Create a list called `master`
2. For each article in the opinion section save the following in a list:
    1. type string :: URL
    2. type string :: Author(s)
    3. type string :: Title
3. For each list representing (2), append to the `master` list
3. Print the following for each element in `master`:
    """ TITLE: {}\nAUTHOR(S): {}\n""".format(< put the title here>, <put the author(s) here>))
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
    soup = BeautifulSoup(response, 'html.parser')
    opinion = soup.find('section', attrs={"data-testid":'block-Opinion'})
    articles = opinion.find_all('div', class_="css-z49qw6")
    master = []
    print(response)
    for article in articles:
        link = article.find('a').get('href')
        author = article.find('a').find('div', class_="css-1j836f9").find('div', class_="css-omcqsq").text
        #author = article.find('div', class_="css-omcqsq")).text
        title = article.find('a').find('h2').text
        master.append([title, author, link])

    for article in master:
        print(""" TITLE: {}\nAUTHOR(S): {}\n""".format(article[0], article[1]))

###################
#     CONFIG      #
###################
cache_file = "nyt.json"
site="nyt"
topic="opinion"
cache = Cache(cache_file)
base = "https://www.nytimes.com/?action=click&contentCollection=undefined&region=TopBar&module=HomePage-Title&pgtype=sectionfront"


#######################
#     RUN PROGRAM     #
#######################

UID = create_id(site, topic)
response = cache.get(UID)
if response == None:
    response = requests.get(base).text
    cache.set(UID, response, 1)

process(response)
