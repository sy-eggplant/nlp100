import math

f = open('hightemp.txt')
num = int(input('>'))
total = len(f.readlines())
f.close()
f = open('hightemp.txt')

line = f.readline()

print(line)
for i in range(math.ceil(total/num)):
    fw = open('output'+str(i)+'.txt','w')
    for j in range(num):
        fw.writelines(line)
        line=f.readline()
        print(line)
    fw.close()

f.close()
