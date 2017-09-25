import re
import extract_from_json

lines = extract_from_json.extract_from_json("イギリス").split("\n")

for line in lines:
    section_line = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
    if section_line is not None:
        print(section_line.group(2), len(section_line.group(1)) - 1)
