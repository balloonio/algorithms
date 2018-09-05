'''
Description
Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

Have you met this question in a real interview?
Example
5 = (101)2 => (1010)2 = 10
'''

class Solution(object):
    # @param {int} x a 32 bit integer
    # @return {int} a 32 bit integer
    # Lintcode will print ctypes.c_int(your_return & 0xffffffff).value as your answer
    def swapOddEvenBits(self, x):
        # Write your code here
        return ( ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1) )
