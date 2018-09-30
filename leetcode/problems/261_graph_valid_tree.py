class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        node2master = [i for i in range(n)]

        for edge in edges:
            n1, n2 = edge
            if n1 == n2:
                continue
            if not self.union(n1, n2, node2master):
                return False

        masters = set()
        for node in range(n):
            master = self.find(node, node2master)
            masters.add(master)
        return True if len(masters) == 1 else False

    def union(self, n1, n2, node2master):
        f1 = self.find(n1, node2master)
        f2 = self.find(n2, node2master)
        if f1 == f2:
            return False
        node2master[f1] = node2master[f2]
        return True

    def find(self, node, node2master):
        path = []
        while node2master[node] != node:
            path += [node]
            node = node2master[node]
        for p in path:
            node2master[p] = node
        return node


"""
The condition for tree as undirected graph:
1. No cycle
2. Only one group of nodes (or one union of nodes)
The second condition is very easy to miss L18 - L22
"""
