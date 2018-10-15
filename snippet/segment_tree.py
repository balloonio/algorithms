class NumArray:
    class Node:
        def __init__(self, value, start, end, left=None, right=None):
            self.value, self.start, self.end = value, start, end
            self.left, self.right = left, right

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.segtree = self.buildSegtree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateSegtree(self.segtree, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(self.segtree, i, j)

    def buildSegtree(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return self.Node(nums[start], start, end)

        mid = (start + end) // 2
        left = self.buildSegtree(nums, start, mid)
        right = self.buildSegtree(nums, mid + 1, end)
        value = 0
        value += left.value if left is not None else 0
        value += right.value if right is not None else 0

        return self.Node(value, start, end, left, right)

    def getSum(self, node, qstart, qend):
        if qstart <= node.start and qend >= node.end:
            return node.value

        mid = (node.start + node.end) // 2
        lval, rval, value = 0, 0, 0
        if mid >= qstart:
            lval = self.getSum(node.left, qstart, qend)
        if mid + 1 <= qend:
            rval = self.getSum(node.right, qstart, qend)

        value += lval + rval
        return value

    def updateSegtree(self, node, i, value):
        if i < node.start or i > node.end:
            return

        if node.start == i and node.end == i:
            node.value = value
            return

        mid = (node.start + node.end) // 2
        if node.start <= i and mid >= i:
            self.updateSegtree(node.left, i, value)
        if mid + 1 <= i and node.end >= i:
            self.updateSegtree(node.right, i, value)

        node.value = 0
        node.value += node.left.value if node.left is not None else 0
        node.value += node.right.value if node.right is not None else 0
        return


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
