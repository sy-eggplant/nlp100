import re
str1 = 'これは漢字を含みます'
words = []
kanji = []

for i in range(len(str1)):
  words += str1[i]
print(words)

for i in range(len(words)):
  result = re.search('[\u4E00-\u9FD0]', words[i])
  if result != None :
    kanji += words[i]


print(kanji)
