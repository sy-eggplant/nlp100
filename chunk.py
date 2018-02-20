class Chunk:

    def __init__(self, dst, morphs):
        self.dst = dst
        # self.srcs = srcs
        self.morphs = morphs

    def __str__(self):
        return 'dst: {}, srcs: {}, morphs: {}'.format(
            self.dst, self.srcs, self.morphs
        )

    def end_of_sentence(self):
        return self.pos1 == '句点'
