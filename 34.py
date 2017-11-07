#「AのB」

import neko_mecab

mapping = neko_mecab.neko_mecab()

noun_phrases = []
count = 0
for i,value in enumerate(mapping):
    if value['surface'] == 'の':
        if mapping[i-1]['pos'] == '名詞' and mapping[i+1]['pos'] == '名詞':
            noun_phrase = mapping[i-1]['surface']
            noun_phrase +='の'
            noun_phrase += mapping[i+1]['surface']
            noun_phrases.append(noun_phrase)

print(noun_phrases)
