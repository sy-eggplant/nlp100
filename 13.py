f1 = open('col1.txt')
f2 = open('col2.txt')

data1 = f1.readlines()
data2 = f2.readlines()
data = []

for (a, b) in zip(data1,data2):
    data += a.rstrip('\r\n')
    data += "\t"
    data += b

f = open('output.txt', 'w')

f.writelines(data)

f.close()
f1.close()
f2.close()
