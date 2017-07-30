f = open('hightemp.txt')
data = f.readlines()

f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')

f1.write(data[0])
f2.write(data[1])

f.close()
f1.close()
f2.close()
