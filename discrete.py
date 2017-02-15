# the index start from 0
class Discrete:

    def __init__(self, f):
        self.f = list(set(f))
        self.f.sort()

    def index(self, a):
        import bisect
        return bisect.bisect_left(self.f, a)

