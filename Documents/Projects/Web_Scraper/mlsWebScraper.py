'''
MLS schedule web crawler
Last edit: 3.14.2018

Some incomplete research led me to believe the MLS provides or requires clubs to use 
a standarized format for MLS team websites. The following code **should** scrape 
the existing schedule from any MLS team webiste and print it to a csv providing the
following information for each posted match:  

-Opponent
-Match Date
-Away or Home
-League or non leauge match

Two items need attention for each iteration, both called out in !!! coments: 

1)The 'page' variable which points the the url of the team schedule you want. Some tested examples:
https://www.soundersfc.com/schedule
https://www.atlutd.com/schedule
https://www.lagalaxy.com/schedule


2) The name of the csv you are printing to--maybe the name of the team who's scheudle you're printing
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
!!!
This is the variable you need to point to the URL of your team's schedule
'''
page = requests.get("https://www.atlutd.com/schedule")

soup = BeautifulSoup(page.content, 'html.parser')

#Find all HTML items that contain match info, start counter
matches = soup.find_all('li', class_='match_item')
counter = 0

#Empty lists that will hold our match info and be translated to dataframe
oppl = []
datel =[]
locl =[]
compl = []

#Loop through all 'match_items' HTML elements, pull out data and append to list
for i in matches:
    meta = matches[counter]
    print(counter)
    opp = meta.find(class_='match_matchup').get_text()
    date = meta.find(class_='match_date').get_text()
    loc = meta.find(class_='match_home_away').get_text()
    comp = meta.find(class_='match_competition').get_text()
    oppl.append(opp)
    datel.append(date)
    locl.append(loc)
    compl.append(comp)
    counter+=1

#Create dataframe, each list = 1 column
games = pd.DataFrame({"Opponent":oppl, 
                      "Date":datel,
                      "Location":locl,
                      "Competition":compl})

'''

!!! 
You'll probably want to name this document based on the team schedule you are printing

'''
games.to_csv('Atlanta_2018.csv')
