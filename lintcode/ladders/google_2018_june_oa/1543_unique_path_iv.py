""" 
Description
Give two integers to represent the height and width of the grid. The starting point is in the upper left corner and the ending point is in the upper right corner. You can go to the top right, right or bottom right. Find out the number of paths you can reach the end. And the result needs to mod 1000000007.

width > 1, height > 1

Have you met this question in a real interview?  
Example
input:
height = 3
width = 3
output:
2
"""


class Solution:
    """
    @param height: the given height
    @param width: the given width
    @return: the number of paths you can reach the end
    """

    def uniquePath(self, height, width):
        # Write your code here

        if not height or not width:
            return 0

        f = [[0] * width for _ in range(height)]
        f[0][0] = 1

        for i in range(width):
            base_x, base_y = 0, i
            for i in range(height - 1):
                x, y = base_x + i, base_y + i
                if self.outBound(width, height, x, y):
                    break
                left = (x, y - 1)
                lefttop = (x - 1, y - 1)
                leftbot = (x + 1, y - 1)

                if not self.outBound(width, height, *left):
                    f[x][y] += f[left[0]][left[1]]
                if not self.outBound(width, height, *lefttop):
                    f[x][y] += f[lefttop[0]][lefttop[1]]
                if not self.outBound(width, height, *leftbot):
                    f[x][y] += f[leftbot[0]][leftbot[1]]

        return f[0][width - 1] % 1000000007

    def outBound(self, width, height, x, y):
        return x < 0 or x >= height or y < 0 or y >= width
