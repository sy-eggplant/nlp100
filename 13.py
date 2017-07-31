f1 = open('col1.txt')
f2 = open('col2.txt')
data = f1.read()
data += f2.read()
f = open('output.txt', 'w')

f.write(data)

f.close()
f1.close()
f2.close()
