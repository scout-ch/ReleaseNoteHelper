This python tool makes it easy to write release notes based on a list in a trello board. The list should contain all the features that will be shipped with an upcoming release. This list will be exported to a markdown file which can be used as a template for writing the release notes. The template contains a title, original description of the feature and a link to the coresponding trello card.

## Setup

 - install python & pip
 - pip install requests
 - pip install mdpdf

https://pypi.org/project/mdpdf/
http://docs.python-requests.org

### Config file

Rename to config.ini.default to config.ini. Change the key and server token to whatever yours is (https://trello.com/app-key).
You will find the ID of your list by opening any card within that list and appending ".json" to the URL. The attribute is called "idList".

## Proposed procedure 

 - Update your Trello list and cards to match your upcoming release
 - Copy the list id
 - Generate output.md by running GetTrelloList.py 
 - Rephrase your Texts, Translate, Publish, ....

 Optional
 - Run MD2PDF.py to create a PDF (output.pdf)

