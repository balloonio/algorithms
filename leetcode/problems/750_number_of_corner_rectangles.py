"""
1.
brutal way 枚举左上角和右下角(所有长方形) 然后check四个角是不是1 时间复杂度 N^2 * N^2 = N^4
思考优化
这道题至少N^2 粗粗感觉是不太可能的 因为遍历matrix就要N^2了
2.
试试看降维攻击 二维转一维 枚举上下边界 H^2 针对每组边界循环遍历边界的一整行
将上边界的所有1点加入set, 遍历下边界时 查看有多少1点的index曾出现在上边界中, X个1点中选2个作为顶点 C(2)(X)
3.
好像还有一个更快一点的答案 大体和二差不多 但是在1比较多的时候有效果拔群
详见 https://leetcode.com/problems/number-of-corner-rectangles/solution/
大体做法就是把row分为密集row和普通row,密集row与其他所有没结算过的row(包括密集row)结算,普通row各自结算
"""


class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return 0

        h, w = len(grid), len(grid[0])
        result = 0
        for top in range(h):
            toprow = grid[top]
            for bot in range(top + 1, h):
                botrow = grid[bot]
                dup1s = 0
                for i in range(w):
                    if toprow[i] == 1 and botrow[i] == 1:
                        dup1s += 1
                if dup1s >= 2:
                    result += dup1s * (dup1s - 1) // 2
        return result
