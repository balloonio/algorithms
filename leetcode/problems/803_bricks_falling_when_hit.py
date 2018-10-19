"""
从联通分量的角度入手 使用并查集去寻找联通分量
但是并查集并不能拆集 那该怎么办呢?
既然不能拆边 那我们不妨从头开始建边吧
那怎样建边可以不妨碍我们计算正确的结果呢
答案就是我们倒序建边
其实逆序这个技巧 在很多题里都有用到 一定要多留意

这个解法时间复杂度 O((N+Q)*α(N))where N = R*CN=R∗C is the number of grid squares,
Q is the length of hits, and \alphaα is the Inverse-Ackermann function.
"""


class Solution:
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        if not grid or not grid[0] or not hits or not hits[0]:
            return [0] * len(hits)

        # a hashmap from brick to father brick for union-find
        # a hashmap from father brick to whether fixed to top or not, non-father bricks will be removed
        self.brick2father = {}
        self.father2fixed = {}
        self.father2count = {}

        # initialize single brick connect component for all bricks
        h, w = len(grid), len(grid[0])
        for i in range(h):
            for j in range(w):
                # this is a brick
                if grid[i][j] == 1:
                    self.brick2father[i, j] = (i, j)
                    self.father2fixed[i, j] = True if i == 0 else False
                    self.father2count[i, j] = 1

        # remove all the hitted bricks
        for i, (x, y) in enumerate(hits):
            if x < 0 or x >= h or y < 0 or y >= w:
                continue
            grid[x][y] -= 1

        # print(self.brick2father, self.father2fixed, self.father2count)

        # union based on the adjacent relationship of bricks on the current board, this gives us some CCs, fixed or not
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    for neari, nearj in self.get_nearby_brick(grid, i, j):
                        self.union(i, j, neari, nearj)
        # print(self.brick2father, self.father2fixed, self.father2count)

        result = []
        for (hitx, hity) in reversed(hits):
            # print(grid)
            grid[hitx][hity] += 1
            if hitx < 0 or hitx >= h or hity < 0 or hity >= w or grid[hitx][hity] == 0:
                result.append(0)
                continue

            # each hit brick is able to act as a linking edge between bricks nearby if any
            # some unfixed CC might be connected to a fixed CC and became fixed, those are the ones that will drop
            new_fixed_total = 0
            for neari, nearj in self.get_nearby_brick(grid, hitx, hity):
                new_fixed = self.union(hitx, hity, neari, nearj)
                new_fixed_total += new_fixed
            if (hitx, hity) in self.father2fixed and self.father2fixed[hitx, hity]:
                new_fixed_total += 1
            result.append(
                new_fixed_total - 1 if new_fixed_total > 0 else 0
            )  # exclude the hit brick

        # print(grid)
        result.reverse()
        return result

    def union(self, x1, y1, x2, y2):
        father1 = self.find(x1, y1)
        father2 = self.find(x2, y2)
        if father1 == father2:
            return 0

        new_fixed = 0
        if self.father2fixed[father1] and self.father2fixed[father2]:
            new_fixed = 0
            father, son = father1, father2
        elif self.father2fixed[father1]:
            new_fixed = self.father2count[father2]
            father, son = father1, father2
        elif self.father2fixed[father2]:
            new_fixed = self.father2count[father1]
            father, son = father2, father1
        else:
            new_fixed = 0
            father, son = father1, father2

        self.brick2father[son] = father
        self.father2count[father] += self.father2count[son]
        self.father2fixed.pop(son)
        self.father2count.pop(son)
        # print("union ", new_fixed, " from ", x1, y1, x2, y2)
        return new_fixed

    def find(self, x, y):
        path = []
        while self.brick2father[x, y] != (x, y):
            path += [(x, y)]
            x, y = self.brick2father[x, y]

        for i, j in path:
            self.brick2father[i, j] = (x, y)
        return x, y

    def get_nearby_brick(self, grid, x, y):
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        h, w = len(grid), len(grid[0])
        for (dx, dy) in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if grid[nx][ny] == 1:
                yield nx, ny


"""
DFS solution
代码量少好多
"""


class Solution:  # noqa: F811
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        # coding, 0:empty, 1:brick, -1:hitted empty, -2:ceil
        m, n = len(grid), len(grid[0])

        def is_connected(i, j):
            return i == 0 or any(
                [
                    0 <= x < m and 0 <= y < n and grid[x][y] == -2
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                ]
            )

        # 把hit的brick都减掉
        for x, y in hits:
            grid[x][y] -= 1
        for i in range(len(grid[0])):
            self.dfs(grid, 0, i)  # 把最上面一行标记为ceil
        res = []
        for x, y in hits[::-1]:
            grid[x][y] += 1
            if grid[x][y] == 1 and is_connected(
                x, y
            ):  # important,要在x,y和其它ceil node相连时才能把他设成-2
                res.append(self.dfs(grid, x, y) - 1)  # 注意要-1！本来hit掉的grid不算新加上的
            else:
                res.append(0)
        return res[::-1]  # 别忘了return前把结果reverse回来

    # 1.把x,y标记为ceil(-2) 2.输出加上x,y后增加的adj brick
    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
            return 0
        res = 1  # note
        grid[x][y] = -2
        for adjX, adjY in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            res += self.dfs(grid, adjX, adjY)
        return res
