import morph
import chunk

sentences = []
sentence = []
chunk_morphs = []
chunk_srcs = [[]]
with open('neko.txt.cabocha', encoding='utf-8') as input_file:
    for line in input_file:
        line_elements = line.split()
        if (line_elements[0] == 'EOS'):
            pass
        elif  (line_elements[0] == '*'):
            c = chunk.Chunk(dst=line_elements[2], secs=chunk_srcs, morphs=chunk_morphs)
            chunk_morphs.clear()
            pass
        else:
            l = line_elements[0].split(',') + line_elements[1].split(',')
            chunk_morphs.append(l[0])
            m = morph.Morph(surface=l[0], base=l[7], pos=l[1], pos1=l[2])
            sentence.append(m)

            if m.end_of_sentence():
                sentences.append(sentence)
                sentence = []

for morph_obj in sentences[2]:
    print(str(morph_obj))
