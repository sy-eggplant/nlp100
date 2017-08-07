import linecache

f = open('hightemp.txt')
num = int(input('>'))
total = len(f.readlines())
surplus = total % num
date_num = total//num+1
date = ""
line = f.readline()
print(line)
for i in range(total):
  line = f.readline()
  date += line
  print(line)


print(date)
f.close()
