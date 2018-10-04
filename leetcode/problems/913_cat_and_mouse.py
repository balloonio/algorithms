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
        n2parents = self.build_node_to_parents(graph)

        # define 2 colors: 1.MOUSE WIN 2.CAT WIN (0.DRAW is considered no color)
        # 2. color all the base case state nodes, and push to queue
        #    queue maintains colored nodes only (DRAW is not queued)

        # 3. For all queued nodes, color their parents with the optimal decision if possible
        #    e.g. If the parent is CAT turn and queued node is CAT WIN, then the parent node is colored CAT
        #    If optimal coloring is not possible, we decrease the unevaluated children of this parent.
        #    When all the children are evaluated and this parent is still not colored, it means all the children are LOSS moves
        #    Only now we color the parent with the LOSS color
        #    e.g. If the parent is CAT turn and queued node is MOUSE WIN,
        #         we cannot determine the color until all children node of this parents are evaluated
        #         (And it is not ganruanteed all the children will be evaluated, because the DRAW ones will not be queue)
        #         (In this case the parent will just stay DRAW because no definite coloring can be done)

    def build_node_to_parents(self, graph):
        for node, connects in enumerate(graph):
            for connect in connects:
                pass
