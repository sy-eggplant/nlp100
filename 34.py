#「AのB」

import neko_mecab

mapping = neko_mecab.neko_mecab()

noun_phrase = []
count = 0
for value in mapping:
    if value['pos'] == '名詞':
        if value['surface'] == 'の':
    count=count+1
    if count = 10:
        break

print(noun_phrase)
