class 2dBinaryIndexedTree:

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.bit = [[0] * (self.num_cols + 1) for _ in range(self.num_rows + 1)]
        
    @staticmethod
    def lowbit(x):
        return x & (-x)

    def update(self, row, col, diff):
        i = row
        while i <= self.num_rows:
            j = col
            while j <= self.num_cols:
                self.bit[i][j] += diff
                j += self.lowbit(j)
            i += self.lowbit(i)
    
    def sum(self, row, col):
        if row == 0 or col == 0:
            return 0
        ret = 0
        i = row
        while i >= 1:
            j = col
            while j >=1:
                ret += self.bit[i][j]
                j -= self.lowbit(j)
            i -= self.lowbit(i)
        return ret
