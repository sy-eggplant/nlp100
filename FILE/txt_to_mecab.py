from natto import MeCab

mc = MeCab()
f_input = open('test.txt')
f_output = open('test.txt.mecab', 'w')

line = f_input.readline()
data = ""
for line in f_input:
    data += mc.parse(line)
    line = f_input.readline()

f_output.writelines(data)

f_input.close()
f_output.close()
