import pymongo
from pymongo import MongoClient
import json
import time



print('''
  ====================================================================================
                                                                                      
      █▀▀█ █▀▀█ █▀▀ █▀▀ █   █ █▀▀█ █▀▀█ █▀▀▄ 　 █▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀ █▀▀ █▀▀█    
      █▄▄█ █▄▄█ ▀▀█ ▀▀█ █▄█▄█ █  █ █▄▄▀ █  █ 　 █ ▀ █ █▄▄█ █  █ █▄▄█ █ ▀█ █▀▀ █▄▄▀    
      █    ▀  ▀ ▀▀▀ ▀▀▀  ▀ ▀  ▀▀▀▀ ▀ ▀▀ ▀▀▀  　 ▀   ▀ ▀  ▀ ▀  ▀ ▀  ▀ ▀▀▀▀ ▀▀▀ ▀ ▀▀    
                                                                                      
  ====================================================================================
''')

########################################################################################################################################

with open('config.json') as file:
    config = json.load(file)
    url = config["url"]

try:
    cluster = MongoClient(url)
    db = cluster["passwords"]
    collection = db["passwords"]
except:
    print('CONNECTION ERROR')
    time.sleep(10)
    exit()

########################################################################################################################################

while True:
    action = input("MANAGER> ")

    if action.lower().strip() == "exit":
        exit()

    elif action.startswith("new"):
        params = action.split('(')[1].split(')')[0]


        service = params.split(',')[0].strip()
        email = params.split(',')[1].strip()
        username = params.split(',')[2].strip()
        password = params.split(',')[3].strip()

        record = {"service": service,
                  "email": email,
                  "username": username,
                  "password": password}

        collection.insert_one(record)
                        
        print('ADDITION SUCCESSFUL')


    elif action.startswith("search"):
        term = action.split('(')[1].split(')')[0].strip()

        results =  collection.find({})
        for result in results:
            if term in result["service"]:
                print(f'''Service: {result["service"]}\nEmail: {result["email"]}\nUsername: {result["username"]}\nPassword: {result["password"]}''')
       





