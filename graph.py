import collections


class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)
    
    def add_edge(self, u, v, value=None):
        self.graph[u].append((v, value))


for u in Graph.graph:
    for v, value in Graph.graph[u]:
        pass
