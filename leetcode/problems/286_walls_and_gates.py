class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        # q : List[ (gate#, step from gate, coordinate) ]
        queue = collections.deque()
        gate_id = 0
        h, w = len(rooms), len(rooms[0])
        gate2visited = []
        for i in range(h):
            for j in range(w):
                if rooms[i][j] == 0:
                    qitem = (gate_id, 0, i, j)
                    queue.append(qitem)
                    visited = set()
                    visited.add((i, j))
                    gate2visited.append(visited)
                    gate_id += 1

        while queue:
            gate, step, x, y = queue.popleft()
            for (nx, ny) in self.get_valid_nearby(x, y, gate2visited[gate], rooms):
                rooms[nx][ny] = min(rooms[nx][ny], step + 1)
                queue.append((gate, step + 1, nx, ny))
                gate2visited[gate].add((nx, ny))
        return

    def get_valid_nearby(self, x, y, visited, rooms):
        h, w = len(rooms), len(rooms[0])
        for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in visited:
                continue
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if rooms[nx][ny] == 0 or rooms[nx][ny] == -1:
                continue
            yield nx, ny


"""
One trick here is that, we can just use one queue for all the gate entry points
However, we need to keep the visited set different for each gate's traversal
Reason is: If all gates can reach this room, we need to know the smallest distance
So we need to let other gate traverse to this room even if one gate already visited
update:之前写的note有点问题,其实只要一个visited就够了,因为所有的门里只有已经有门在现在这个门之前
visit了这个地方,说明其距离一定是小于等于当先这个BFS level的
这是一个典型的多起点多终点的bfs,和assign bike那道题联合记忆
再更正一下....好像有些时候是需要分开visited set的,比如说bike那道题,一个人找到了最近的自行车之后就停住了
但是其他人还需要继续找,如果公用一个visited set的话其他人找车时候的距离是要受到已经结束的那个人
的visited set影响的
"""
