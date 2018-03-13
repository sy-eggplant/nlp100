import morph
import chunk

sentences = []
sentence = []
chunk_morphs = []
c_srcs = {}
with open('neko.txt.cabocha', encoding='utf-8') as input_file:
    for line in input_file:
        line_elements = line.split()
        if (line_elements[0] == 'EOS'):
            c_srcs = {}
            pass
        elif  (line_elements[0] == '*'):
            if '-' in line_elements[2]:
                c_dst = -1
            else:
                c_dst = int(line_elements[2][:1])
            c_srcs.append(line_elements[1])
            print(c_srcs)
            c = chunk.Chunk(dst=c_dst, morphs=chunk_morphs)
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
