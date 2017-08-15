f = open('hightemp.txt')
f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')

line = f.readline()
col1_data = []
col2_data = []

while line:
    words = (line.split())
    col1_data += words[0::4]
    col1_data += "\n"
    col2_data += words[1::4]
    col2_data += "\n"
    line=f.readline()

f1.writelines(col1_data)
f2.writelines(col2_data)

f.close()
f1.close()
f2.close()
