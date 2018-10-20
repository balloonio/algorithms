"""
2D平面上，有m个人（P），n辆自行车(B)，还有空白（O）满足以下条件
1.m < n
2.不存在两个人，到同一辆自行车距离相等, 距离用abs(x1-x2) + abs(y1-y2)定义
3.每个人尽量找离自己最近的自行车，一旦某辆自行车被占，其他人只能找别的自行车。

例
OPOBOOP
OOOOOOO
OOOOOOO
OOOOOOO
BOOBOOB

红色的人找到第一行的自行车，距离最近。
蓝色的人离第一行自行车最近，但自行车已经被红色人占有，所以他只能找离他第二近的，右下角的自行车
就是一个2维数组里的有人和自行车，要每个人匹配到一辆自行车，人和自行车的距离越短越好，没有距离相同的情况。
就是算出所有的距离然后放到heap里慢慢pop出来，记录下人和车的状态就可以了。
"""

import heapq
import collections

"""
最小堆存距离pair的做法 m个人n个车
时间复杂度 O(MNlogMN)
空间复杂度 O(MN)
"""


def assign_bike(board):
    if not board or not board[0]:
        return []

    unused_bike = set()
    ppl_remain = set()
    heap = []  # heap of ( dist, person coor (i,j), bike coor (i,j))

    h, w = len(board), len(board[0])
    for i in range(h):
        for j in range(w):
            if board[i][j] == "P":
                ppl_remain.add((i, j))
            elif board[i][j] == "B":
                unused_bike.add((i, j))

    for (pi, pj) in ppl_remain:
        for (bi, bj) in unused_bike:
            # calculate the distance for this pair
            dist = abs(pi - bi) + abs(pj - bj)
            heapq.heappush(heap, (dist, (pi, pj), (bi, bj)))

    result = []
    while heap and ppl_remain and unused_bike:
        dist, ppl, bike = heapq.heappop(heap)
        while heap and (ppl not in ppl_remain or bike not in unused_bike):
            dist, ppl, bike = heapq.heappop(heap)
        result.append([ppl, bike])
        unused_bike.remove(bike)
        ppl_remain.remove(ppl)
    return result


"""
多源BFS的做法 每个人是一个源 全部加入一个队列 但是分别用不同的各自的visited set
原因是 如果一个人找到车了不继续找的 其他继续在找车的人的路径距离就不对了, 会受到之前这个人的visited
set的影响而skip一些点
时间复杂度 O(M* size of board) 因为最差情况的话所有人要走遍board
空间复杂度 O(M* size of board)
"""


def assign_bike_bfs(board):
    if not board or not board[0]:
        return []
    bikedppl = set()
    usedbike = set()

    q = collections.deque()  # put coordinate into the queue with distance to ppl
    h, w = len(board), len(board[0])

    p2visited = collections.defaultdict(set)
    pplcnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == "P":
                pplcnt += 1
                p2visited[(i, j)].add((i, j))
                q.append((i, j, 0, i, j))  # coordinate i, j, distance, person i, j

    result = []
    while q and len(bikedppl) < pplcnt:
        coor_i, coor_j, dist, ppl_i, ppl_j = q.popleft()
        # this person already assigned, no need to keep search for him
        if (ppl_i, ppl_j) in bikedppl:
            continue
        # found an unsed bike for this person
        if board[coor_i][coor_j] == "B" and (coor_i, coor_j) not in usedbike:
            result.append([(ppl_i, ppl_j), (coor_i, coor_j)])
            usedbike.add((coor_i, coor_j))
            bikedppl.add((ppl_i, ppl_j))
            continue
        for nx, ny in get_nearby_xy(board, coor_i, coor_j):
            if (nx, ny) in p2visited[(ppl_i, ppl_j)]:
                continue
            q.append((nx, ny, dist + 1, ppl_i, ppl_j))
    return result


def get_nearby_xy(board, x, y):
    h, w = len(board), len(board[0])
    for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        yield nx, ny


"""
以下为testcase 实际印证了两个时间复杂度的优劣
"""

board = [
    "OPOBOOOPOOOOOO",
    "OOOBOOOOOBOOOO",
    "OOOOOOOOOPOOOO",
    "BOOOOOOOOOOPOO",
    "BOOBOOBOOOPOOB",
]

for _ in range(7):
    board += board

# python3 assign_bike.py  1.42s user 0.12s system 99% cpu 1.557 total
assign_bike(board)

# python3 assign_bike.py  12.21s user 0.41s system 99% cpu 12.700 total
assign_bike_bfs(board)
