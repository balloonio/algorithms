# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = collections.deque()
        self.stack.append( [nestedList, 0] )

    def next(self):
        """
        :rtype: int
        """
        s = self.stack
        ni, idx = s[-1]
        s[-1][1] += 1
        return ni[idx]

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            ni, idx = s[-1]
            if idx >= len(ni):
                s.pop()
            elif ni[idx].isInteger():
                return True
            else:
                next_list = ni[idx].getList()
                s[-1][1] += 1
                s.append( [next_list, 0] )
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Keep in mind that some times its hard to determine whether stack has integer
# or full of blank list. Therefore, it is better to keep the logic in hasNext()
