"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        if not A:
            return None

        root_val = max(A)
        A.append(math.inf)
        val2node = self.copy_node(A)

        # strictly desc mono stack
        mono_stack = collections.deque()

        for i, num in enumerate(A):
            # pop top until stack qualify for mono stack
            popped = None
            while mono_stack and mono_stack[-1] <= num:
                popped = mono_stack.pop()
                before_popped = mono_stack[-1] if mono_stack else None
                # for popped, before_popped is the first larger on left, num is the first larger on right
                if before_popped is None or num < before_popped:
                    val2node[num].left = val2node[popped]
                else:
                    val2node[before_popped].right = val2node[popped]

            mono_stack.append(num)

        return val2node[root_val]

    def copy_node(self, A):
        val2node = {}
        for num in A:
            val2node[num] = TreeNode(num)

        return val2node
