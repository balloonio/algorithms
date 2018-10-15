# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = collections.deque()
        result = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            result.append(stack[-1].val)
            if stack[-1].right:
                stack.append(stack[-1].right)
                while stack[-1].left:
                    stack.append(stack[-1].left)
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
        return result
