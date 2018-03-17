# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

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
x = [] # 順位
y = [] # 出現頻度

for k, v in sorted(dct_words.items(), key=lambda x: -x[1]):
    # k=頻出数、v=単語
    count = count + 1
    x.append(count)
    y.append(str(v))

plt.bar( x, y )
#plt.xticks(x,words)
plt.show()
