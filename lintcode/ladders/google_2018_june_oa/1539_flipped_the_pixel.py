""" 
Description
An image is stored as a 2D byte array (byte[][] image), and each pixel is a bit (0 or 1).Now we're going to flip the pixels of each row symmetrically.First flipped each byte of each row symmetrically, and then flipped each byte separately

1.both 1 and 0 are integers
2.The Byte is not empty

Have you met this question in a real interview?  
Example
Given byte[] []=
[[1,0,1,1,0],[0,1,1,0,1],[1,1,0,1,0], [0,0,1,0,0]]
Return:
[[1,0,0,1,0],[0,1,0,0,1],[1,0,1,0,0],[1,1,0,1,1]]
"""


class Solution:
    """
    @param Byte: 
    @return: return the answer after flipped
    """

    def flippedByte(self, Byte):
        # Write your code here
        if not Byte or not Byte[0]:
            return None

        for b in Byte:
            b.reverse()
            for i in range(len(b)):
                b[i] = 1 if b[i] == 0 else 0

        return Byte
