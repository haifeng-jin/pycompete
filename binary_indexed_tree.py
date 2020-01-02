# the index start from 1
class BinaryIndexedTree:

    def __init__(self, n):
        self.f = [0] * (n + 3)
        self.n = n + 2

    def sum(self, pos):
        i = pos
        s = 0  #initialize result
        while i > 0:
            s += self.f[i]
            i -= i & (-i)
        return s
 
    def update(self, pos ,diff):
        i = pos
        while i <= self.n:
            self.f[i] += diff
            i += i & (-i)

