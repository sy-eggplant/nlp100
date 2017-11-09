# 連続した名詞

import neko_mecab

mapping = neko_mecab.neko_mecab()

nouns = []
count = 0
flag = 0

while count<len(mapping):
    value=mapping[count]
    if value['pos'] == '名詞':
        noun=value['surface']
        while 1:
            if mapping[count+1]['pos'] == '名詞':
                noun += mapping[count+1]['surface']
                count=count+1
                flag=1
            else:
                count=count+1
                break
        if flag==1:
            nouns.append(noun)
            flag=0
    else:
        count=count+1

print(nouns)
