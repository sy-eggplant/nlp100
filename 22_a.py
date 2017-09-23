import re
import extract_from_json

lines = extract_from_json.extract_from_json("イギリス").split("\n")

for line in lines:
    category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category_line is not None:
        print(category_line.group(1))
