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

        level_head = root
        last_level_head = None
        while level_head:
            level_curr = level_head
            is_curr_left = True
            while level_curr:
                if not last_level_head:
                    level_curr.next = None
                else:
                    level_curr.next = (
                        last_level_head.right if is_curr_left else last_level_head.left
                    )
                    last_level_head = (
                        last_level_head.next if is_curr_left else last_level_head
                    )
                is_curr_left = not is_curr_left
                level_curr = level_curr.next
            last_level_head = level_head
            level_head = level_head.left
