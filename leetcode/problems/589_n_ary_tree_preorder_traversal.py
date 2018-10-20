"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def __init__(self):
        # trace stack - put the current node on it
        self.trcstack = collections.deque()
        # progress stack - put the progress of the corresponding recursion level
        self.cntstack = collections.deque()

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        trcstack = self.trcstack
        cntstack = self.cntstack

        result = []
        trcstack.append(root)
        cntstack.append(0)

        while trcstack:
            if trcstack[-1] is None:
                trcstack.pop()
                cntstack.pop()
                continue
            if cntstack[-1] == 0:
                result.append(trcstack[-1].val)
            if cntstack[-1] >= len(trcstack[-1].children):
                trcstack.pop()
                cntstack.pop()
                continue
            next_son = cntstack[-1]
            cntstack[-1] += 1
            trcstack.append(trcstack[-1].children[next_son])
            cntstack.append(0)

        return result


# recursion
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root, result=None):
        """
        :type root: Node
        :rtype: List[int]
        """
        need_return = False
        if result is None:
            need_return = True
            result = []

        if not root:
            return None if not need_return else []

        result.append(root.val)
        for son in root.children:
            self.preorder(son, result)

        if need_return:
            return result
