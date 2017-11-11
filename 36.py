# 頻出文字

import neko_mecab

mapping = neko_mecab.neko_mecab()

dct_words = {}
words = []
count = 0

for value in mapping:
    if not value['surface'] in dct_words:
        dct_words[value['surface']] = 1
    else:
        count = dct_words[value['surface']]
        dct_words[value['surface']] = count+1

for k, v in sorted(dct_words.items(), key=lambda x: -x[1]):
    words.append(str(k) + ": " + str(v))

print(words)
