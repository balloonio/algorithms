# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.col2vals = collections.defaultdict(list)
        self.smallest, self.largest = 0, 0
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = collections.deque()
        q.append( (root, 0) )
        
        while q:
            node, col = q.popleft()
            self.smallest = min(col, self.smallest)
            self.largest = max(col, self.largest)
            self.col2vals[col].append(node.val)
            if node.left:
                q.append( (node.left, col-1) )
            if node.right:
                q.append( (node.right, col+1) )
        
        result = []
        for col in range(self.smallest, self.largest + 1):
            result.append( self.col2vals[col] )
        return result