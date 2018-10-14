class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return
        evenidx, oddidx = 0, 1
        n = len(A)

        while evenidx < n and oddidx < n:
            # increment evenidx until any odd is found on evenidx
            while evenidx < n and A[evenidx] % 2 == 0:
                evenidx += 2
            # similarly increment oddidx
            while oddidx < n and A[oddidx] % 2 == 1:
                oddidx += 2
            if evenidx < n and oddidx < n:
                A[evenidx], A[oddidx] = A[oddidx], A[evenidx]
                evenidx += 2
                oddidx += 2
        return A
