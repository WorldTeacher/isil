url="https://sigel.staatsbibliothek-berlin.de/api/org.jsonld?q=&last"
import requests
import json
import sys
import os
import time

#if folder does not exist, create it
if not os.path.exists("data"):
    os.makedirs("data")

data=requests.get(url)
data=data.json()

for i in data['member']:
    print(i['name'])
    #if file does not exist, create it
    if not os.path.exists("data/"+i['_id']+".json"):
        with open("data/"+i['_id']+".json", "w") as f:
            json.dump(i, f, indent=4)
    #if file exists, exit script
    else:
        print("File already exists")
        sys.exit()
print(data['view']['next'])

    # with open("data/"+i['@id'].split("/")[-1]+".json", "w") as outfile:
'''
make a function that opens the url, saves the data in a json file and returns the next url
use the function in a while loop using
'''
def metadata_scrape(url):
    data=requests.get(url)
    data=data.json()
    for i in data['member']:
        print(i['name'])
        #if file does not exist, create it
        if not os.path.exists("data/"+i['_id']+".json"):
            with open("data/"+i['_id']+".json", "w") as f:
                json.dump(i, f, indent=4)
    
    time.sleep(1)
    next_url=data['view']['next']
    last_url=data['view']['last']
    return next_url


#     return data[view']['next']

while url:
    url=metadata_scrape(url)

