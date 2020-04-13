import json
import requests
import sys

# retrieving credentials from ArangoDB tutorial service
def getTempCredentials():
  with open("creds.dat","r+") as cacheFile: 
    contents = cacheFile.read()
    if len(contents) > 0:
      #. check if credentials are still valid
      login = json.loads(contents)
      url = "https://"+login["hostname"]+":"+str(login["port"])
      conn =""
      try: 
        conn = Connection(arangoURL=url, username=login["username"], password=login["password"],)
        print("Reusing cached credentials.")
        return login
      except:
        print("Credentials expired.")
        pass # Ignore and retrieve new 
    
    # Retrieve new credentials from Foxx Service
    print("Requesting new temp credentials.")
    url = 'https://5904e8d8a65f.arangodb.cloud:8529/_db/_system/alpha/tutorialDB'
    x = requests.post(url, data = "{}")

    if x.status_code != 200:
      print("Error retrieving login data.")
      sys.exit()
    # Caching credentials
    cacheFile.truncate() 
    cacheFile.write(x.text)
  return json.loads(x.text)