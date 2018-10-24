"""
DFS或BFS
先构造图
通过collections.defaultdict(dict)来构造邻接表
self.sym2edges[x][y] = div 表示x和y相连接 div是x/y的ratio
在寻求query结果的过程中
如果x和y都在记忆化结果里, 那他们应当有相同的unit,直接两两之间的ratio计算出结果
如果x y任意一个不在记忆化结果里, 那我们就通过dfs或是bfs,根据所有的edge去马克这相连的一整片图,
把他们马克成同一个unit x或是y
如果马克完还是没有在记忆化结果里,说明input里没有这个数
如果马克完 x和y都在记忆化结果里 但是unit不一样 说明x和y其实不是来自同一片图 两两没有conversion
"""


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not equations or not values:
            return [-1.0] * len(queries)

        self.sym2edges = collections.defaultdict(dict)
        eqvals = zip(equations, values)

        # 构造图的邻接表
        for (x, y), div in eqvals:
            self.sym2edges[x][y] = div
            self.sym2edges[y][x] = 1 / div

        # 构造记忆化ratio结果
        self.sym2val = collections.defaultdict(list)
        result = []
        for (x, y) in queries:
            if x not in self.sym2val:
                # go find x if input has x
                if x in self.sym2edges:
                    self.convert_all_connect(x, 1, x)
                    # self.convert_all_connect_bfs(x, 1, x)
            if y not in self.sym2val:
                # go find y if input has y
                if y in self.sym2edges:
                    self.convert_all_connect(y, 1, y)
                    # self.convert_all_connect_bfs(y, 1, y)
            # now both should in result
            if x not in self.sym2val or y not in self.sym2val:
                result.append(-1.0)
                continue
            xratio, xunit = self.sym2val[x]
            yratio, yunit = self.sym2val[y]
            if xunit != yunit:
                result.append(-1.0)
                continue
            result.append(xratio / yratio)
        return result

    def convert_all_connect(self, sym, ratio, unit):
        if sym in self.sym2val:
            return
        self.sym2val[sym] = [ratio, unit]
        for next_sym, next_ratio in self.sym2edges[sym].items():
            self.convert_all_connect(next_sym, ratio / next_ratio, unit)
        return

    def convert_all_connect_bfs(self, sym, ratio, unit):
        if sym in self.sym2val:
            return
        q = collections.deque()
        q.append((sym, ratio, unit))

        while q:
            (sym, ratio, unit) = q.popleft()
            self.sym2val[sym] = [ratio, unit]
            for next_sym, next_ratio in self.sym2edges[sym].items():
                if next_sym in self.sym2val:
                    continue
                q.append((next_sym, ratio / next_ratio, unit))
        return


"""
union find
base_unit_conversion is like union
evaluate is like find
"""


class Solution:  # noqa: F811
    def __init__(self):
        self.var2unit = {}  # to base unit
        self.var2mult = {}  # to multiplier

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        if not queries:
            return []

        for i, eq in enumerate(equations):
            first, second = eq
            if first not in self.var2unit and second not in self.var2unit:
                self.var2unit[first] = second
                self.var2mult[first] = values[i]
                self.var2unit[second] = second
                self.var2mult[second] = 1
            elif first in self.var2unit and second in self.var2unit:
                self.base_unit_conversion(first, second, values[i])
            elif first in self.var2unit:
                multiplier, unit = self.evaluate(first)
                self.var2mult[second] = multiplier / values[i]
                self.var2unit[second] = unit
            else:
                multiplier, unit = self.evaluate(second)
                self.var2mult[first] = multiplier * values[i]
                self.var2unit[first] = unit
        result = []
        for query in queries:
            first, second = query
            first_mult, first_unit = self.evaluate(first)
            second_mult, second_unit = self.evaluate(second)

            if first_unit == "?" or second_unit == "?" or first_unit != second_unit:
                result += [-1.0]
            else:
                result += [first_mult / second_mult]
        return result

    def base_unit_conversion(self, first, second, ratio):
        first_mult, first_unit = self.evaluate(first)
        second_mult, second_unit = self.evaluate(second)
        if first_unit == second_unit:
            return
        # 1st multi * 1st unit / (2nd multi * 2nd unit) = ratio
        # => 1st unit = ratio * 2st mult / 1nd multi in terms of 2nd unit
        self.var2unit[first_unit] = second_unit
        self.var2mult[first_unit] = ratio * second_mult / first_mult
        return

    def evaluate(self, unit):
        if unit not in self.var2unit:
            return -1.0, "?"
        multiplier = 1
        while unit != self.var2unit[unit]:
            multiplier *= self.var2mult[unit]
            unit = self.var2unit[unit]
        return multiplier, unit


"""
使用单源多点最短路算法
"""


class Solution(object):  # noqa : F811
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        # build graph edges between each symbol with weight
        vertx2id = {}
        for i, eq in enumerate(equations):
            x, y = eq
            if x not in vertx2id:
                vertx2id[x] = len(vertx2id)
            if y not in vertx2id:
                vertx2id[y] = len(vertx2id)

        n = len(vertx2id)
        dist = [
            [math.inf] * n for _ in range(n)
        ]  # dist[x][y] gives the multiplier: symbol x = dist[x][y] * symbol y
        path = [
            [""] * n for _ in range(n)
        ]  # path[x][y] gives the last vertex before y to achieve the curr dist[x][y]
        for i, eq in enumerate(equations):
            x, y = eq
            x, y = vertx2id[x], vertx2id[y]
            dist[x][y] = values[i]
            dist[y][x] = 1 / values[i]
            path[x][y] = x

        for intermediate in range(n):
            for start in range(n):
                for end in range(n):
                    if (
                        dist[start][end]
                        > dist[start][intermediate] * dist[intermediate][end]
                    ):
                        dist[start][end] = (
                            dist[start][intermediate] * dist[intermediate][end]
                        )
                        path[start][end] = intermediate

        result = []
        for query in queries:
            x, y = query
            if x not in vertx2id or y not in vertx2id:
                result.append(-1.0)
            else:
                x, y = vertx2id[x], vertx2id[y]
                result.append(dist[x][y] if dist[x][y] != math.inf else -1.0)
        return result


"""
DFS
"""


class Solution:  # noqa : F811
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not equations:
            return [-1.0] * len(queries)

        graph = collections.defaultdict(dict)

        for (st, ed), val in zip(equations, values):
            graph[st][st] = graph[ed][ed] = 1.0
            graph[st][ed] = val
            graph[ed][st] = 1 / val

        def dfs(st, ed, visited):
            # if st in visited: return -1.0 #reach a circle
            visited.add(st)
            if ed in graph[st]:
                return graph[st][ed]

            for nb in graph[st]:
                if nb not in visited:
                    tmp = dfs(nb, ed, visited)
                    if tmp != -1.0:
                        return graph[st][nb] * tmp
            return -1.0

        ret = []
        for st, ed in queries:
            if st not in graph or ed not in graph:
                ret.append(-1.0)
            else:
                visited = set()
                ret.append(dfs(st, ed, visited))
        return ret
