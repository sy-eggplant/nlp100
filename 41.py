import morph
import chunk

m_objs = []
m_obj = []
srcs = {}
sentences = []
sentence = []
c = None
with open('neko.txt.cabocha', encoding='utf-8') as input_file:
    for line in input_file:
        line_elements = line.split()
        if line_elements[0] == 'EOS':
            #一文の終わり
            if c is not None:
                sentence.append(c)
            if len(sentence)>0:
                sentences.append(sentence)
            m_objs.append(m_obj)
            #初期化
            m_obj = []
            srcs = {}
            sentence = []
            c = None

        elif  line_elements[0] == '*':
            #文節の終わり
            if c is not None:
                sentence.append(c)
            # chunkの要素を取得
            dst = int(line_elements[2].replace('D',''))
            #src（かかり元文節インデックス番号）
            src = int(line_elements[1])
            #chunk作成
            c = chunk.Chunk(morphs=[], srcs=[],dst=dst)
            if dst == -1:
                srcs = None
            else:
                if dst in srcs:
                    srcs[dst].append(src)
                else:
                    srcs[dst] = [src]
                if src in srcs:
                    c.srcs.append(srcs[src])
            


        else:
            #単語ごと
            l = line_elements[0].split(',') + line_elements[1].split(',')
            if l[0] == '記号':
                pass
            else:
                m = morph.Morph(surface=l[0], base=l[7], pos=l[1], pos1=l[2])
                m_obj.append(m)
                c.morphs.append(m)

for morph_obj in m_objs[2]:
    print(str(morph_obj))

target = sentences[7]
for chunk_obj in target:
    if chunk_obj.dst is not None:
        print(chunk_obj.surface() + ' => ' + target[chunk_obj.dst].surface())
    else:
        print(chunk_obj.surface())
