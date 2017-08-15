from collections import Counter

f = open('hightemp.txt')
line = f.readline()
words = []
pref =[]

while line:
    words = (line.split())
    pref += words[0::4]
    line=f.readline()

f.close
print(pref)

counter = Counter(pref)

for word, cnt in counter.most_common():
    print (word,cnt)
