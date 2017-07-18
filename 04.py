str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = str1.split(' ')
dict = {}

for i in range(len(words)):
  if i in (1, 5, 6, 7, 8, 9, 15, 16, 19):
    dict[i+1] = words[i][:2]
  else:
    dict[i+1] = words[i][:1]

print(dict)
