str1 = 'パトカー'
str2 = 'タクシー'
str3 = ''

for i in range(1,5):
  str3 += (str1[i-1])
  str3 += (str2[i-1])

print(str3)

str3 = ''
for (a,b) in zip(str1,str2):
  str3 += a+b

print(str3)
