# This DFS solution has some problem on testcase
# [[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]]
class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        # let's define state as (cat position, mouse position, mouse_turn)
        # and the value 0: draw, 1: mouse, 2: cat
        self.memo = {}
        self.graph = graph
        return self.move(2, 1, True)

    def move(self, cat, mouse, mouse_turn):
        memo = self.memo
        graph = self.graph
        key = (cat, mouse, mouse_turn)
        # searched before, return searched result
        if key in memo:
            return memo[key]
        memo[key] = 0

        # last step for winning condition
        # cat: 1 step away from mouse in cat turn
        # mouse: 1 step away from hole in mouse turn
        if mouse_turn:
            for nextplc in graph[mouse]:
                if nextplc == 0:
                    memo[key] = 1
                    return 1
        else:
            for nextplc in graph[cat]:
                if nextplc == 0:
                    continue
                if nextplc == mouse:
                    memo[key] = 2
                    return 2

        # initialize as draw
        # cat: if any next place with mouse turn is mouse loss, cat win here
        # mouse: if any next place with cat turn is cat loss, mouse win here
        if mouse_turn:
            res = 2
            for nextplc in graph[mouse]:
                if nextplc == cat:
                    continue
                result_there = self.move(cat, nextplc, False)
                if result_there == 1:
                    res = 1
                    break
                if result_there == 0:
                    res = 0
            memo[key] = res
            return memo[key]

        res = 1
        for nextplc in graph[cat]:
            if nextplc == 0:
                continue
            result_there = self.move(nextplc, mouse, True)
            if result_there == 2:
                res = 2
                break
            if result_there == 0:
                res = 0
        memo[key] = res
        return memo[key]


# The below bottom-up coloring solution is based on the LeetCode official solution
# This one can pass all the cases so far
DRAW, MOUSE, CAT = 0, 1, 2


class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        # define state
        # (cat position, mouse position, mouse turn/cat turn)
        # 1. build a map { each state node : its parent nodes }
        #    N's parent nodes = all the state node that can reach N in the next turn
        n2parents, p2degree = self.build_node_to_parents(graph)
        # print(p2degree)
        # p2degree = self.count_node_degree(graph)
        # print(p2degree)
        # define 2 colors: 1.MOUSE WIN 2.CAT WIN (0.DRAW is considered no color)
        # 2. color all the base case state nodes, and push to queue
        #    queue maintains colored nodes only (DRAW is not queued)
        color = collections.defaultdict(int)
        n = len(graph)
        for cat_pos in range(n):
            # status when mouse is at hole
            color[cat_pos, 0, MOUSE] = MOUSE
            color[cat_pos, 0, CAT] = MOUSE
            # status when cat caught mouse and not at hole
            if cat_pos != 0:
                color[cat_pos, cat_pos, MOUSE] = CAT
                color[cat_pos, cat_pos, CAT] = CAT

        queue = collections.deque()
        for status, c in color.items():
            if c != DRAW:
                queue.append(status)

        # 3. For all queued nodes, color their parents with the optimal decision if possible
        #    e.g. If the parent is CAT turn and queued node is CAT WIN, then the parent node is colored CAT
        #    If optimal coloring is not possible, we decrease the unevaluated children of this parent.
        #    When all the children are evaluated and this parent is still not colored, it means all the children are LOSS moves
        #    Only now we color the parent with the LOSS color
        #    e.g. If the parent is CAT turn and queued node is MOUSE WIN,
        #         we cannot determine the color until all children node of this parents are evaluated
        #         (And it is not ganruanteed all the children will be evaluated, because the DRAW ones will not be queue)
        #         (In this case the parent will just stay DRAW because no definite coloring can be done)

        while queue:
            status = queue.popleft()
            curr_cat, curr_mouse, curr_turn = status
            for parent in n2parents[status]:
                par_cat, par_mouse, par_turn = parent
                # if current node is same color as the previous parent turn
                # meaning this node is CAT win and previously it was cat TURN from a node that can reach this one
                # mark the parent node the winning color
                if color[parent] != DRAW:
                    continue
                if color[status] == par_turn:
                    color[parent] = color[status]
                    queue.append(parent)
                # no winning move can be made for now, lets decrease the parents node degree
                # when it reaches 0, it means all moves were losing move, then mark the opposite color
                else:
                    p2degree[parent] -= 1
                    if p2degree[parent] == 0:
                        color[parent] = CAT if par_turn == MOUSE else MOUSE
                        queue.append(parent)

        return color[2, 1, MOUSE]

    def count_node_degree(self, graph):
        p2degree = collections.defaultdict(int)
        n = len(graph)
        for cat_pos in range(n):
            for mouse_pos in range(n):
                p2degree[cat_pos, mouse_pos, MOUSE] = len(graph[mouse_pos])
                p2degree[cat_pos, mouse_pos, CAT] = len(graph[cat_pos]) - graph[
                    cat_pos
                ].count(0)
        return p2degree

    def build_node_to_parents(self, graph):
        # status node to the parents status nodes that can reach itself in the next turn
        # (cat 5, mouse 0, cat turn) => (cat 5, mouse 2, mouse turn) if 0 and 2 are connected in graph
        n2parents = collections.defaultdict(set)
        p2degrees = collections.defaultdict(int)
        n = len(graph)
        # enumerate all status nodes
        for cat_pos in range(n):
            if cat_pos == 0:
                continue
            for mouse_pos in range(n):
                # cat turn to previous mouse turn move
                for connect in graph[mouse_pos]:
                    n2parents[cat_pos, mouse_pos, CAT].add((cat_pos, connect, MOUSE))
                    p2degrees[cat_pos, connect, MOUSE] += 1
                # mouse turn to previous cat turn move
                for connect in graph[cat_pos]:
                    if connect != 0:
                        n2parents[cat_pos, mouse_pos, MOUSE].add(
                            (connect, mouse_pos, CAT)
                        )
                        p2degrees[connect, mouse_pos, CAT] += 1
        return n2parents, p2degrees


"""
L129 skip the ones already colored
L163 L164 skip 0 cat location, otherwise the p2degrees count would be wrong here
or just simply count the indegree separately as in count_node_degree
"""
