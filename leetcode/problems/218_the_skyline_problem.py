class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []

        building_edges = [] # [ (position, is_end, height) ]
        for i, building in enumerate(buildings):
            start, end, height = building
            building_edges += [ (start, False, height, i) ]
            building_edges += [ (end, True, height, i) ]

        building_edges.sort()
        curr_buildings = []
        removed = set()
        outline = []

        for edge in building_edges:
            coor, is_end, height, bid = edge
            if not is_end:
                # new building coming, add to heap
                self.push_edge(curr_buildings, edge)
            else:
                # old building gone, rm from heap, we can do this before pop, add to removed set
                removed.add(bid)
            # get the top until top has not been removed
            while curr_buildings and self.top_bid(curr_buildings) in removed:
                heapq.heappop(curr_buildings)
            # current tallest building at coor
            tallest = self.top_h(curr_buildings) if curr_buildings else 0
            if not outline:
                outline.append( [coor, tallest] )
            elif outline[-1][0] == coor:
                outline[-1][1] = max(tallest, outline[-1][1])
            elif outline[-1][1] != tallest:
                outline.append( [coor, tallest] )
        return outline
    
    def top_h(self, tall_heap):
        _, height, bid = tall_heap[0]
        return height

    def top_bid(self, tall_heap):
        _, height, bid = tall_heap[0]
        return bid

    def push_edge(self, tall_heap, edge):
        coor, is_end, height, bid = edge
        heap_item = (-height, height, bid)
        heapq.heappush(tall_heap, heap_item)
