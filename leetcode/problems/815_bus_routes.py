class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        if not routes:
            return -1

        stop2bus = collections.defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop2bus[stop].add(bus)

        queue = collections.deque()
        visited_bus = set()
        visited_stop = set()
        # push the first level buses valaible from routes
        for bus in stop2bus[S]:
            queue.append((bus, 1))
            visited_bus.add(bus)

        while queue:
            bus, seq = queue.popleft()
            for stop in routes[bus]:
                if stop == T:
                    return seq
                if stop in visited_stop:
                    continue
                visited_stop.add(stop)
                for next_bus in stop2bus[stop]:
                    if next_bus in visited_bus:
                        continue
                    queue.append((next_bus, seq + 1))
                    visited_bus.add(next_bus)
        return -1


"""
First thought:
this is some traversal sort of thing, BFS should work
every bus is like a node
every bus stop is like a linkage between different buses
we start from bus stop S, which means all the buses available at that stop is the first level nodes
"""
