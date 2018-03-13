class Chunk:

    def __init__(self, morphs, srcs, dst):
        self.morphs = morphs
        self.srcs = srcs
        self.dst = dst

    def __str__(self):
        return 'morphs: {}, srcs: {}, dst: {}'.format(
            ' / '.join([str(m) for m in self.morphs]), self.srcs, self.dst
        )

    def surface(self):
        return ''.join(m.surface for m in self.morphs)
