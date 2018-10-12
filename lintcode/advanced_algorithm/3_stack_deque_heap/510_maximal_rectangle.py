class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """

    def maximalRectangle(self, matrix):
        # write your code here

        if not matrix or not matrix[0]:
            return 0

        prerow_sum = self.get_prerow_sum(matrix)
        result = 0
        for row in prerow_sum:
            area = self.get_row_max(row)
            result = max(area, result)

        return result

    def get_row_max(self, heights):
        indices_stack = []
        area = 0
        heights.append(0)
        for index, height in enumerate(heights + [-1]):
            while indices_stack and heights[indices_stack[-1]] >= height:
                popped_index = indices_stack.pop()
                left_index = indices_stack[-1] if indices_stack else -1
                width = index - left_index - 1
                area = max(area, width * heights[popped_index])
            indices_stack.append(index)
        return area

    def get_prerow_sum(self, m):
        ps = [[] for _ in range(len(m))]

        for i in range(len(m)):
            ps[i] = [
                (((ps[i - 1][x] if i - 1 >= 0 else 0) + 1) if m[i][x] else 0)
                for x in range(len(m[0]))
            ]

        return ps
