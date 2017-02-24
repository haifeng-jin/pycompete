class UnionFind:
    def __init__(self,n):
        self.parent=[0]*n
        self.rank=[0]*n
        self.count = n
        for i in range(0,n):
            self.parent[i]=i
            self.rank[i]=0
    def find(self,x):
        self.validate(x)
        while x!=self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x
    def validate(self,x):
        n=len(self.parent)
        if x<0 or x>=n:
            raise IndexError
    def connected(self,x,y):
        return self.find(x)==self.find(y)
    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)
        if rootX==rootY:
            return
        if self.rank[rootX]<self.rank[rootY]:
            self.parent[rootX]=rootY
        elif self.rank[rootX]>self.rank[rootY]:
            self.parent[rootY]=rootX
        else:
            self.parent[rootY]=rootX
            self.rank[rootX]+=1
        self.count-=1
