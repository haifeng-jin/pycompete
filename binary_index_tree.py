# the index start from 1
class BITree:

    def __init__(self, n):
        self.f = [0]*(n+3)
        self.n = n + 2

    def sum(self, pos=None):
        if not pos:
            pos = self.n
        i = pos
        s = 0  #initialize result
        while i > 0:
            s += self.f[i]
            i -= i & (-i)
        return s
 
    def update(self, pos ,value):
        i = pos
        while i <= self.n:
            self.f[i] += value
            i += i & (-i)

