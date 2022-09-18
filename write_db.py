import sqlite3
import glob
from time import sleep
import random
from turtle import home
import json5 as json
data_path = "data/"
database="isil.db"
fields={'001A':'tbd',
        '001B':'tbd',
        '001D':'tbd',
        '001U':'unicode-encode',
        '002@':'tbd',
        '003@':'tbd',
        '008H':'sigil',
        '009Q':'urls',
        '029@':'shortname',
        '029A':'longname',
        '032P':'Address',
        '035B':'contact_data',
        '035E':'bib_type/verbund',
        '035I':'leihverkehr. zs mgl',
        '047A':'statusse'}

def extract_data(file):
    with open(file, "r") as f:
        data=json.load(f)
    metadata=data['data']
    adress=metadata['032P']

    print(adress.text)



# filelist=glob.glob(data_path+"*.json")
# for file in filelist:
#     extract_data(file)
#     sleep(10)


def connect_db():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    return c, conn

def create_table():
    c, conn = connect_db()


def drop_table():
    c, conn = connect_db()
    c.execute("DROP TABLE IF EXISTS GENERALDATA")
    c.execute("DROP TABLE IF EXISTS ADDRESS")
    c.execute("DROP TABLE IF EXISTS CONTACT_DATA")
    c.execute("DROP TABLE IF EXISTS STATUS")
    c.execute("DROP TABLE IF EXISTS SIGEL")
    conn.commit()
    conn.close()
def generate_id():
    numbers="0123456789"
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    id=""
    for i in range(0, 6):
        id+=numbers[random.randint(0, 9)]
        id+=letters[random.randint(0, 51)]
    print(id)
    return id
def insert_data():
    files=glob.glob("data/*.json")
    for file in files:
        with open(file, "r") as f:
            data=json.load(f)
    # with open("data/DE-Frei129.json", "r") as f:
    #     data=json.load(f)
        metadata=data['data']
        for field in metadata:
            if field in fields:
                print(field, metadata[field])
        
        
        # adress=metadata['032P'][0]
        # sigils=metadata['008H'][0]
        # bib=metadata['035E'][0]
        # organization=metadata['029@'][0][0]['a']
        # name=metadata['029A'][0][0]['a']
        # adress_street=adress[0]['a']
        # adress_city=adress[1]['b']
        # adress_country=adress[2]['d']
        # adress_zip=adress[3]['e']
        # adress_state=adress[4]['f']
        # try:
        #     opening_hours=adress[5]['i']
        # except:
        #     opening_hours=""
        # try:
        #     adress_n=adress[6]['k']
        #     adress_w=adress[7]['l']
        # bib_type=bib[4]['f']
        # bib_verbund=bib[3]['d']
        # sigils_zdb=sigils[0]['a']
        # sigils_dbs=sigils[1]['b']
        # sigils_ezb=sigils[4]['f']
        # sigils_bib=sigils[2]['d']
        # sigil_isil=sigils[3]['e']

        #print(adress_country, adress_city, adress_street, adress_zip, adress_state, opening_hours, adress_n, adress_w, sigils_zdb, sigils_dbs, sigils_ezb, sigils_bib, sigil_isil)
        c, conn = connect_db()
        id=generate_id()
        c.execute("INSERT INTO library (name, id,type,organization) VALUES (?,?,?,?)", (name,id,bib_type,organization))

        c.execute("INSERT INTO adress (country, city, street, zipcode, state, opening_hours, geo_n, geo_w,id) VALUES (?,?,?,?,?,?,?,?,?)", (adress_country, adress_city, adress_street, adress_zip, adress_state, opening_hours, adress_n, adress_w, id))
        c.execute("INSERT INTO sigils (zdb, dbs, ezb, sigel,isil,id,verbundsystem) VALUES (?,?,?,?,?,?,?)", (sigils_zdb, sigils_dbs, sigils_ezb, sigils_bib, sigil_isil,id,bib_verbund))
        conn.commit()
        conn.close()
def delete_data():
    c, conn = connect_db()
    #delete all data from tables
    c.execute("DELETE FROM library")
    c.execute("DELETE FROM adress")
    c.execute("DELETE FROM sigils")

    c.execute("DELETE FROM addititonal_data")
    conn.commit()
    conn.close()

def print_files():
    with open("data/DE-Frei129.json", "r") as f:
        data=json.load(f)
        metadata=data['data']
        dbs=""
        zdb=""
        ezb=""
        sigel=""
        isil=""
        for field in metadata:
            if field in fields:
                if field =='001A':
                    for content in metadata[field][0][0]:
                        date_created=content
                if field =='001B':
                    for content in metadata[field]:
                        date_modified=content[0]
                        timestamp=content[1]['t']
                if field =='001D':
                    for content in metadata[field]:
                        date_something=content[0][0]
                if field =='001U':
                    for content in metadata[field]:
                        encoding=content[0][0]
                if field =='002@':
                    for content in metadata[field]:
                        something=content[0][0]
                if field =='003@':
                    for content in metadata[field]:
                        something_2=content[0][0]
                if field =='008H':
                    for content in metadata[field]:
                        #go through all sigils
                        for sigil in content:
                            #if the first part of the dict matches the given letter, it is the sigil for the zdb
                            #get the content of the dict
                            for key in sigil:
                                if key=='a':
                                    zdb=sigil[key]
                                if key=='b':
                                    dbs=sigil[key]
                                if key=='d':
                                    sigel=sigil[key]
                                if key=='e':
                                    isil=sigil[key]
                                if key=='f':
                                    ezb=sigil[key]
                if field =='009Q':
                    for content in metadata[field]:
                        temp_dict = {k:v for subdict in content for k, v in subdict.items()} 
                        if temp_dict.get("z", None) == 'A':
                            homepage=temp_dict.get("u", None)
                        if temp_dict.get("z", None) == 'B':
                            opac=temp_dict.get("u", None)
                

                            


                        
                    # content=metadata[field]
                    # print('date created:', metadata[field])
                #print(field, metadata[field])
if __name__=="__main__":
    # create_table()
    #insert_data()
    #drop_table()
    #generate_id()
    # delete_data()
    print_files()