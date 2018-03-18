import morph_a
import chunk_a

sentences = []
sentence = []
srcs_dic = {}
_chunk = None
with open('neko.txt.cabocha', encoding='utf-8') as input_file:
    for line in input_file:
        line_elements = line.split()
        if line_elements[0] == '*':
            if _chunk is not None:
                sentence.append(_chunk)

            src = int(line_elements[1])
            dst = int(line_elements[2][:-1])
            if dst != -1:
                if dst in srcs_dic:
                    srcs_dic[dst].append(src)
                else:
                    srcs_dic[dst] = [src]
            else:
                dst = None

            _chunk = chunk_a.Chunk(morphs=[], srcs=srcs_dic.get(line_elements[1]), dst=dst)
        elif line_elements[0] == 'EOS':
            if _chunk is not None:
                sentence.append(_chunk)
            if len(sentence) > 0:
                sentences.append(sentence)
                srcs_dic = {}
            _chunk, sentence = None, []
        else:
            l = line_elements[0].split(',') + line_elements[1].split(',')
            _morph = morph_a.Morph(surface=l[0], base=l[7], pos=l[1], pos1=l[2])
            _chunk.morphs.append(_morph)

target = sentences[7]
for chunk_obj in target:
    if chunk_obj.dst is not None:
        print(chunk_obj.surface() + ' => ' + target[chunk_obj.dst].surface())
    else:
        print(chunk_obj.surface())
