#!/usr/bin/python3

class WQU:
    def __init__(self, N):
        self.Id = list(range(N))
        self.sz = [1] * N

    def root(self, p):
        while(self.Id[p] != p):
            p = self.Id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        rp = self.root(p)
        rq = self.root(q)
        if self.sz[rp] < self.sz[rq]:
            self.Id[rp] = rq
            self.sz[rq] += self.sz[rp]
        else:
            self.Id[rq] = rp
            self.sz[rp] += self.sz[rq]
