import read
import json
import re

json_dict = read.read_wikipedia()
json_str = json.dumps(json_dict, ensure_ascii=False)
print(json_str.split("\n"))
#print(json_dict)
for line in json_str:
    print(line)
