import read_wiki
import re
import json
json = read_wiki.read_wikipedia()
m = json.search("Category")
print (m)
