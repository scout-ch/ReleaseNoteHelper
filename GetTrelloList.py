# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json
import codecs
import os
import configparser
from datetime import date

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

if os.path.exists("index.md"):
  os.remove("index.md")

f = codecs.open("index.md", "a", "utf-8")

# Version Params (change these)
version = "1.25.0"
lang = "de"
today = date.today()
date = today.strftime("%d.%m.%Y")

# Header
f.write("---\n")
f.write("title: MiData Release Notes " + version + "\n")
f.write("date: '" + date + "'\n")
f.write("categories: '" + version.rsplit('.', 1)[0] + "'\n")
f.write("slug: " + version.replace(".", "-") + "\n")
f.write("lang: " + lang + "\n")
f.write("---\n\n")

# Features
for card in cards:
    f.write("# " + card['name'] + "\n")
    description = card['desc'].replace("*in", "\*in")
    description = description.replace("\\\\*in", "\*in")
    description = description.replace("der*die", "der\*die")
    description = description.replace("die*der", "die\*der")
    f.write(description + "\n\n")
    f.write("[Mehr informationen](" + card['shortUrl'] + ")\n\n")

f.close()