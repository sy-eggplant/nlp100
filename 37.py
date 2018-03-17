# 頻出文字上位10位

import neko_mecab
import matplotlib.pyplot as plt

mapping = neko_mecab.neko_mecab()

dct_words = {}
words = {}
count = 0

for value in mapping:
    if not value['surface'] in dct_words:
        dct_words[value['surface']] = 1
    else:
        count = dct_words[value['surface']]
        dct_words[value['surface']] = count+1

count = 0
x = []
words = []
y = []
for k, v in sorted(dct_words.items(), key=lambda x: -x[1]):
    words.append(str(k))
    y.append(str(v))
    count = count + 1
    x.append(count)
    if count == 10:
        break

plt.bar( x, y )
plt.xticks(x,words)
plt.show()
