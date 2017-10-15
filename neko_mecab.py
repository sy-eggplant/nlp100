

def neko_mecab():
    f = open('neko.txt.mecab', 'r')
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
    f.close()
    return mapping



# print(neko_mecab())
