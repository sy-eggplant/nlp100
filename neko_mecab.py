

def neko_mecab():
    f = open('neko.txt.mecab', 'r')
    mapping = []
    for line in f:
        num = line.find('EOS')
        if num == 0:
            sent = line.lstrip('EOS')
            line = sent
            if len(line.split("\t")) >= 2:
                hyou ,other = line.split("\t")
                other = other.split(",")
                dic = {
                    'surface': hyou,
                    'base': other[6],
                    'pos': other[0],
                    'pos1': other[1]
                }
                mapping.append(dic)
        if num == -1:
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


#neko_mecab()
print(neko_mecab())
