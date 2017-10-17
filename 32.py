import neko_mecab

mapping = neko_mecab.neko_mecab()

verbs = []
for value in mapping:
    if value['pos'] == '動詞':
        verbs.append(value['base'])

print(verbs)
