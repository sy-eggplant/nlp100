import linecache

f = open('hightemp.txt')

num = input('>')
target_line = linecache.getline('hightemp.txt', int(num))
print(target_line)
f.close()
