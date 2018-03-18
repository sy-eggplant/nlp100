import morph

m_objs = []
m_obj = []

with open('neko.txt.cabocha', encoding='utf-8') as input_file:
    for line in input_file:
        line_elements = line.split()
        if line_elements[0] == 'EOS':
            m_objs.append(m_obj)
            m_obj = []
            pass
        elif  line_elements[0] == '*':
            pass
        else:
            l = line_elements[0].split(',') + line_elements[1].split(',')
            m = morph.Morph(surface=l[0], base=l[7], pos=l[1], pos1=l[2])
            m_obj.append(m)

for morph_obj in m_objs[2]:
    print(str(morph_obj))
