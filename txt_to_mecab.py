from natto import MeCab

mc = MeCab()
f_input = open('neko.txt')
f_output = open('neko2.txt.mecab', 'w')

line = f_input.readline()
data = ""
for line in f_input:
    data += mc.parse(line)
    line = f_input.readline()

f_output.writelines(data)

f_input.close()
f_output.close()
