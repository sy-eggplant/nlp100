import re
import extract_from_json

lines = extract_from_json.extract_from_json("イギリス").split("\n")
temp_dict = {}


for line in lines:
    temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S)
    if temp_line is not None:
        temp_dict[temp_line.group(1)] = temp_line.group(2)

for k, v in sorted(temp_dict.items(), key=lambda x: x[1]):
    print(k, v)
