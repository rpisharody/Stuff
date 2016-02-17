#!/usr/bin/python3

class QF:
    def __init__(self, N):
        self.Id = list(range(N))

    def connected(self, p, q):
        return self.Id[p] == self.Id[q]

    def union(self, p, q):
        pid = self.Id[p]
        qid = self.Id[q]
        for ii in range(len(self.Id)):
            if self.Id[ii] == pid:
                self.Id[ii] = qid
