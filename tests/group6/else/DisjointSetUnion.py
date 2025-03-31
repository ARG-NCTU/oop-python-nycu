class DisjointSetUnion:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
