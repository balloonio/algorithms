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

        inedge = {}
        candidates = []
        for i, edge in enumerate(edges):
            father, son = edge
            if son in inedge:
                candidates += [inedge[son], edge]
                edges[i] = None  # 删除这个有两个father的边
                break
            inedge[son] = edge

        n = len(edges)
        for node in range(1, n + 1):
            self.node2father[node] = node

        for edge in edges:
            if not edge:
                continue
            father, son = edge
            # 有环
            if not self.union(father, son):
                # 所有点只有一个father
                if not candidates:
                    return edge
                # 有点有两个father, 而且删掉一个边以后发现
                # 还是有环, 这时候我们应该删除第二个边
                else:
                    return candidates[0]
        # 没有环, 那么证明我们之前删除的那个边是对的
        return candidates[1]

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


"""
Unionfind:
这是一个有向图问题

先考虑有没有环:

如果图有环, 那么又有两种情况:

要么是没有任何一个点有两个parent, 这种情况下我们就得删除形成环的那个边
5 <- 1 -> 2
     ^    |
     |    v
     3 <- 4
要么就是有一个点有两个parent, 这种情况下我们也是要删除形成环的那个边. 在这里要注意一下,
因为我们的程序默认是先删除有两个parent的那个点的后面的一条边, 所以在这种情况下我们要返回另一条边,
例如在这个例子中我们会先删除(5 -> 1)这条边, 但这个是错误的, 我们应该删除(3 -> 1)这条边, 这个会在程序里处理
5 -> 1 -> 2
     ^    |
     |    v
     3 <- 4
图没有环, 那么肯定是有一个点有两个parent, 删掉一个即可

      1
     /  \
    v    v
   2 ---> 3
"""
