import morph

sentences = []
sentence = []
with open('neko.txt.cabocha', encoding='utf-8') as input_file:
    for line in input_file:
        line_elements = line.split()
        if (line_elements[0] == 'EOS') | (line_elements[0] == '*'):
            pass
        else:
            l = line_elements[0].split(',') + line_elements[1].split(',')
            m = morph.Morph(surface=l[0], base=l[7], pos=l[1], pos1=l[2])
            sentence.append(m)

            if m.end_of_sentence():
                sentences.append(sentence)
                sentence = []

for morph_obj in sentences[2]:
    print(str(morph_obj))
