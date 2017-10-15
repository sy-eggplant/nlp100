f = open('neko.txt.mecab', 'r')
g = open('neko.mecab_dic.txt', 'w')

mapping = []

for line in f:
    if line.find("EOS") == -1:
        hyou ,other = line.split("\t")
        other = other.split(",")
        dic = {
            'surface': hyou,
            'base': other[6],
            'pos': other[0],
            'pos1': other[1]
        }
        mapping.append(dic)

print(mapping)
f.close()
g.close()
