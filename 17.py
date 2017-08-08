import linecache

target_line = linecache.getline('hightemp.txt', 1)
words = list(target_line)

s = set([])

for i in range(len(words)):
    s.add(words[i])

print(s)
