# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json
import codecs
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

url = "https://api.trello.com/1/lists/" + config['Trello']['ListId'] + "/cards"

query = {
   'key': config['Trello']['Key'],
   'token': config['Trello']['Token']
}

response = requests.request(
   "GET",
   url,
   params=query
)
#print(response.text)
cards  = json.loads(response.text)

if os.path.exists("output.md"):
  os.remove("output.md")

f = codecs.open("output.md", "a", "utf-8")
f.write("# Release Notes - MiData\n\n")

for card in cards:
    f.write("## " + card['name'] + "\n")
    f.write(card['desc'] + "\n\n")
    f.write("Mehr informationen: " + card['shortUrl'] + "\n\n")

f.close()