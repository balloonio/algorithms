"""
onsite最后一轮的面试题。其他轮都没啥发的必要就不发了。题目是这样的 给你一个list的长方形
每个长方形面积不一样，但是你要取个点，这个点可以是任何长方形里的。但是要你每次取点的概率都是一样的。
不会因为长方形大小而不同。不算难，但是我对概率的不太擅长

assume 每个长方形不重叠。 先按照面积（建一个prefix sum数组）， 随机得到一个矩形。
再按照那个矩形的长和宽随机得到一个点。
我问了最优解 思路是这样没错，但是随机每个矩阵得到的概率是不一样的。再填这一部就好
"""

import random

# 1. one rectangle, given the top left vertex and bot right vertex
#                   return the top left vertex coordinate of the randomed point
def single_rectangle_sampling(x1, y1, x2, y2):
    if x1 >= x2 or y1 <= y2:
        raise InputError("input error")

    h, w = y1 - y2, x2 - x1
    randnum = random.randint(0, h * w - 1)
    x = x1 + randnum % w
    y = y1 - randnum // w
    return x, y


# a list of non-overlapping rectangles given the same way as in 1.
# (x1,y1,x2,y2)
def multiple_rectangle_sampling(recs):
    if not recs:
        return -1
    ps = [0]
    for rec in recs:
        x1, y1, x2, y2 = rec
        h, w = y1 - y2, x2 - x1
        area = h * w
        ps.append(ps[-1] + area)

    total_area = ps[-1]
    randnum = random.randint(0, total_area - 1)

    # binary search to find the first i so that ps[i] > randnum
    start, end = 0, len(ps) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if ps[mid] > randnum:
            end = mid
        else:
            start = mid
    rectangle = None
    if ps[start] > randnum:
        rectangle = recs[start - 1]
        randnum = randnum - ps[start - 1]
    else:
        rectangle = recs[end - 1]
        randnum = randnum - ps[end - 1]
    x1, y1, x2, y2 = rectangle
    h, w = y1 - y2, x2 - x1
    x = x1 + randnum % w
    y = y1 - randnum // w
    return x, y


# 如果长方形之间有叠加怎么办?
# 考虑几种情况
# 1. 长方形相互之间的高一样不一样? 一样的话 我们可以先merge interval 然后作为没重叠的长方形来处理
# 2. 长方形的叠加会不会一定覆盖一个横向的中轴向? 如果有的话, 我们可以像skyline那样做, 地平线上地平线下 两个skyline
# 3. 都没有的话我们是不是可以分割矩形
# 第二轮：第一问：二维坐标中给了一个矩形，要求生成一个任意一个坐标点，位置在矩形内。第二问，二维坐标中有多个不重叠的矩形，
# 要求生成一个任意坐标点，位置在这些矩形中，要求生成的点落在各矩形的概率相同。followup：如果提供这两个function，
# isOverlap(rectangle a, rectangle b) 判断两个矩形是否重合, split(rectangle a, rectangle b) 若两矩形重合，
# 将两个矩形分成互补重叠的小矩形， 问题是: 如何在上述的矩形中加入一个新的矩形。.
"""
我们可以根据x轴二分来排除掉一定不重合的长方形
如果你的右边界在我的左边界的左边 那我们一定不重合
所以我们可以先按照右边界排序 然后二分找到第一个右边界在我的左边界右边的长方形
从这个长方形开始往后所有的长方形 有可能和我重合 有可能不重合 因为你的左边界有可能在我的右边界的右边
所以我们把从这个长方形开始以及往后的所有长方形 再按照左边界排序 找到第一个左边界在我的右边界的右边的
那从这个开始再往后的 都是不要的 因为一定不会重合
所以中间这一段是由x轴判断出来的有可能和我重合的长方形
我们再把这些个 按照y轴用一样的逻辑走一遍
找出一定重合的那些个 然后使用api
"""


"""
以下是一些testcase
"""

rec0 = (0, 5, 1, 1)
rec1 = (3, 9, 5, 7)
rec2 = (6, 5, 8, 0)

recs = [rec0, rec1, rec2]
print(multiple_rectangle_sampling(recs))
