# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return

        rightmost = None
        if root.left and root.right:
            root.left.next = root.right
        rightmost = root.right if root.right else root.left
        if root.next:
            rightmost.next = self.get_leftmost_son(root.next)

        self.connect(root.right)
        self.connect(root.left)

    def get_leftmost_son(self, head):
        while head:
            if head.left:
                return head.left
            if head.right:
                return head.right
            head = head.next
        return None


# L25 L26 Pay attention to the traverse order. Right has to go before left
