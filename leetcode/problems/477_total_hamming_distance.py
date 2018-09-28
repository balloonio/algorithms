class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        largest = max(nums)
        bitmask = 1
        hamsum = 0

        while bitmask <= largest:
            bit0, bit1 = 0, 0
            for num in nums:
                if num & bitmask:
                    bit1 += 1
                else:
                    bit0 += 1
            hamsum += bit0 * bit1
            bitmask <<= 1
        return hamsum


# L22 bitmask <<= 1 not bitmask << 1
# int is immutable
