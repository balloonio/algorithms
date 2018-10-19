"""
union find
base_unit_conversion is like union
evaluate is like find
"""


class Solution:
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
