# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

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

count = 0 # 前回の値
index = 0 # xのため
num = 0 # 単語の種類数
x = [] # 棒グラフのため
words = [] # 単語の種類数
y = [] # 頻出数

for k, v in sorted(dct_words.items(), key=lambda x: -x[1]):
    # k=頻出数、v=単語
    if count == str(v):
    # 同じ出現頻度であれば単語の種類を追加
        num = num + 1
    else:
        index = index + 1
        x.append(index)
        y.append(num)
        words.append(count)
        num = 0
        count = str(v)

# 最後はいらないのでいれる
index = index + 1
x.append(index)
y.append(num)
words.append(count)

plt.bar( x, y )
plt.xticks(x,words)
plt.show()
