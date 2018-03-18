class Chunk:

    def __init__(self, morphs, srcs, dst):
        self.morphs = morphs
        self.srcs = srcs
        self.dst = dst
    def surface(self):
        return ''.join(m.surface for m in self.morphs)
