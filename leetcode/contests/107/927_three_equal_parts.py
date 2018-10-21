"""
核心思想的话
I.  三个部分1的数量应该是一样的
II. 三个部分的最右边的0的数量是确定的, 由第三个部分的尾端来确定,因为他的尾端就是整个数组的尾端
"""


class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        onesum = sum(A)
        if onesum % 3 != 0:
            return [-1, -1]
        if onesum == 0:
            return [0, len(A) - 1]

        onesize = onesum // 3
        alen = len(A)

        thirdsum = 0
        rightj, leftj = None, None
        # going from right to left
        for i in range(alen - 1, -1, -1):
            thirdsum += A[i]
            if thirdsum < onesize:
                continue
            if thirdsum > onesize:
                break
            rightj = i if rightj is None else rightj
            leftj = i

        # count the trailing zeroes on the third part
        trailing0 = 0
        for num in reversed(A):
            if num == 1:
                break
            trailing0 += 1
        resultj = leftj + trailing0
        if resultj > rightj:
            return [-1, -1]

        righti, lefti = None, None
        firstsum = 0
        for i in range(alen):
            firstsum += A[i]
            if firstsum < onesize:
                continue
            if firstsum > onesize:
                break
            lefti = i if lefti is None else lefti
            righti = i

        resulti = lefti + trailing0
        if resulti > righti:
            return [-1, -1]

        if not self.binary_same(A[: resulti + 1], A[resultj:]):
            return [-1, -1]
        if not self.binary_same(A[resulti + 1 : resultj], A[resultj:]):
            return [-1, -1]

        return [resulti, resultj]

    def binary_same(self, arr1, arr2):
        arr1.reverse()
        arr2.reverse()
        for i in range(min(len(arr1), len(arr2))):
            if arr1[i] != arr2[i]:
                return False
        return True
