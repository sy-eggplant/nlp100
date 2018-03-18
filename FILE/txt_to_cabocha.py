import CaboCha

f_input = open('neko.txt')
f_output = open('neko.txt.cabocha', 'w')

c = CaboCha.Parser()
line = f_input.readline()
data = ""
for line in f_input:
    tree = c.parse(line)
    data += tree.toString(CaboCha.FORMAT_LATTICE)
    line = f_input.readline()
    tree = ""

f_output.writelines(data)

f_input.close()
f_output.close()


# tree =  c.parse(sentence)
#
# print tree.toString(CaboCha.FORMAT_TREE)
# print tree.toString(CaboCha.FORMAT_LATTICE)
