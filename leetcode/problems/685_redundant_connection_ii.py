class Solution:
    def __init__(self):
        self.node2father = {}

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []

        n = len(edges)
        for node in range(1, n + 1):
            self.node2father[node] = node

        for edge in edges:
            father, son = edge
            if not self.union(father, son):
                return edge
        return []

    def union(self, father, son):
        if father == son:
            return False
        parent1 = self.find(father)
        parent2 = self.find(son)

        if parent1 == parent2:
            return False
        self.node2father[parent2] = parent1
        return True

    def find(self, node):
        path = []
        while node != self.node2father[node]:
            path += [node]
            node = self.node2father[node]

        for p in path:
            self.node2father[p] = node
        return node
