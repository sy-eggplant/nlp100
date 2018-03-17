class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def neko_cabocha():
        f = open('neko.txt.cabocha', 'r')
        mapping = []
        for line in f:
            num = line.find('EOS')
            num_1 = line.find('*')
            if num == 0 or num_1 == 0:
                sent = line.lstrip('EOS')
                line = sent
                if len(line.split("	")) >= 2:
                    hyou ,other = line.split("	")
                    other = other.split(",")
                    dic = {
                        'surface': hyou,
                        'base': other[6],
                        'pos': other[0],
                        'pos1': other[1]
                    }
                    mapping.append(dic)
            elif num == -1 or num_1 == -1:
                hyou ,other = line.split("	")
                other = other.split(",")
                dic = {
                    'surface': hyou,
                    'base': other[6],
                    'pos': other[0],
                    'pos1': other[1]
                }
                mapping.append(dic)
        f.close()
        return mapping

    def set_num(f_line):
        f = open('neko.txt.cabocha', 'r')
        mapping = []
        for line in f:
            num = line.find('EOS')
            num_1 = line.find('*')
            if num == 0 or num_1 == 0:
                sent = line.lstrip('EOS')
                line = sent
                if len(line.split("	")) >= 2:
                    hyou ,other = line.split("	")
                    other = other.split(",")
                    dic = {
                        'surface': hyou,
                        'base': other[6],
                        'pos': other[0],
                        'pos1': other[1]
                    }
                    mapping.append(dic)
            elif num == -1 or num_1 == -1:
                hyou ,other = line.split("	")
                other = other.split(",")
                dic = {
                    'surface': hyou,
                    'base': other[6],
                    'pos': other[0],
                    'pos1': other[1]
                }
                mapping.append(dic)
        f.close()
        return mapping



print(neko_cabocha())
