import re

str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = str1.split(' ')
num = 0

for i in range(len(words)):
  # if words[i].isalpha():
  #   num = len(words[i])+num*10
  # else:
  #   num = len(words[i])-1+num*10
  words[i] = re.sub(re.compile("[!-/:-@[-`{-~]"), '', words[i])
  num = len(words[i])+num*10

print(num)
