"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if len(preorder) != len(inorder):
            return None  # error
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        curr_val = preorder[0]
        inorder_idx = None
        for i, val in enumerate(inorder):
            if val == curr_val:
                inorder_idx = i
                break

        curr_node = TreeNode(curr_val)
        left_size = inorder_idx

        left_pre = preorder[1 : 1 + left_size]
        right_pre = preorder[1 + left_size :]
        left_in = inorder[:left_size]
        right_in = inorder[inorder_idx + 1 :]

        curr_node.left = self.buildTree(left_pre, left_in)
        curr_node.right = self.buildTree(right_pre, right_in)

        return curr_node


"""
tip for binary tree problems
draw an example binary tree with actual values
write down the two representation
observe the pattern

For the following binary tree:
        B
      /  \
     Z    S
    / \  / \
   H  J F   D

pre : [B,  Z,H,J,  S,F,D]
in  : [H,Z,J,  B,  F,S,D]
notice something here?
"""
