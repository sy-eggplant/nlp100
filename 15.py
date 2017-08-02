import linecache

f = open('hightemp.txt')

num = input('>')
total = len(f.readlines())
target_line = linecache.getline('hightemp.txt', total-int(num)+1)
print(target_line)
f.close()
