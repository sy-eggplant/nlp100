def mecab_reader(mecabfile):
    sentences = []
    sentence = []
    for line in mecabfile:
        if line == "EOS\n":
            if len(sentence) > 0:
                sentences.append(sentence)
            sentence = []
        else:
            surface, features = line.split("\t")
            features = features.split(",")
            dic = {
                'surface': surface,
                'base': features[6],
                'pos': features[0],
                'pos1': features[1]
            }
            sentence.append(dic)
    return sentences


f = open('neko.txt.mecab', 'r')
g = open('neko.mecab_dic.txt', 'w')

sentences = []
sentence = []

for line in f:
    if line == "EOS\n":
        if len(sentence) > 0:
            sentences.append(sentence)
        sentence = []
    else:
        features = line.split("\t")
        features = features.split(",")
        dic = {
            'surface': surface,
            'base': features[6],
            'pos': features[0],
            'pos1': features[1]
        }
        sentence.append(dic)

#sentences = mecab_reader(f)

# for s in sentences:
#     # print str(s).decode("string-escape")
#     g.write(str(s).decode("string-escape") + "\n")

f.close()
g.close()
