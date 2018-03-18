class Chunk:

    def __init__(self, morphs, srcs, dst):
        self.morphs = morphs
        self.srcs = srcs
        self.dst = dst

    def surface(self):
        return ''.join(m.surface for m in self.morphs)

    def has_noun(self):
        result = False
        for m in self.morphs:
            if m.pos == '名詞':
                result = True
        return result

    def has_verb(self):
        result = False
        for m in self.morphs:
            if m.pos == '動詞':
                result = True
        return result
