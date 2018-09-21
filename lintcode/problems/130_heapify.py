""" 
Description
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

Challenge
O(n) time complexity

Clarification
What is heap?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.

What is heapify?
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
Return any of them.
"""


class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """

    def heapify(self, A):
        # write your code here
        last_son = len(A) - 1
        last_father = (last_son - 1) // 2

        for i in reversed(range(last_father + 1)):
            self.siftdown(A, i)

    def siftdown(self, A, father):
        n = len(A)

        while father * 2 + 1 < n:
            son1 = father * 2 + 1
            son2 = father * 2 + 2
            minson = min(A[son1], A[son2]) if son2 < n else A[son1]

            if A[father] <= minson:
                return

            if A[son1] == minson:
                A[father], A[son1] = A[son1], A[father]
                father = son1
            else:
                A[father], A[son2] = A[son2], A[father]
                father = son2
