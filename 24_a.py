import re
import extract_from_json

lines = extract_from_json.extract_from_json("イギリス").split("\n")

for line in lines:
    file_line = re.search("(File|ファイル):(.*?)\|", line)
    if file_line is not None:
        print(file_line.group(2))
