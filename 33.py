import neko_mecab

mapping = neko_mecab.neko_mecab()

nouns = []
for value in mapping:
    if value['pos1'] == 'サ変接続' and value['pos'] == '名詞':
        nouns.append(value['base'])

print(nouns)
