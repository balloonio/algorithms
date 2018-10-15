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
        result = []
        while root:
            if not root.left:
                result.append(root.val)
                root = root.right
            else:
                #找到先驱节点 这里要注意在不停往右的过程中如果遇到了root 说明是我们自己插进去的 那就不能继续了 再继续就不是先驱节点了
                last_before = root.left
                while last_before.right and last_before.right.val != root.val:
                    last_before = last_before.right
                
                if not last_before.right:
                    last_before.right = root
                    root = root.left
                else:
                    last_before.right = None
                    result.append(root.val)
                    root = root.right
        return result
