import linecache

target_line = linecache.getline('hightemp.txt', 1)
words = list(target_line)
print(words)
