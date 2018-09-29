class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if not wall or not wall[0]:
            return 0

        dist2edge = collections.defaultdict(int)
        wallh = len(wall)
        wallw = sum(wall[0])

        for row in wall:
            dist = 0
            for width in row:
                dist += width
                dist2edge[dist] += 1

        minbricks = wallh
        for dist, edges in dist2edge.items():
            if dist == wallw:
                continue

            minbricks = min(minbricks, wallh - edges)

        return minbricks


"""
用map数每个位置有几条分界线，分界线最多的胜出
"""
