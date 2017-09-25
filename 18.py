f = open('hightemp.txt')
line = f.readline()
words = []
temp =[]

while line:
    words = (line.split())
    temp += words[2::4]
    line=f.readline()

temp.sort();
f.close
print(temp)
