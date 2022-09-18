#open data folder
#go through all files and access data
#extract fieldnames to a list

import json5 as json
import os

fields = []
for filename in os.listdir("data"):
    if filename.endswith(".json"):
        with open("data/"+filename, "r") as f:
            data=json.load(f)
            metadata=data['data']
            for field in metadata:
                
                if field not in fields:
                    fields.append(field)
#store fieldnames in a file
with open("fields.txt", "w") as f:
    for field in fields:
        f.write(field+"\n")
