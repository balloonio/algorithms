'''
Description
Given n, m and an one-dimensional array arr. Take some elements from arr to get the XOR of them, and there will be 2^n results(n is the size of arr). Please calculate the number of results that greater than m ,and output the answer modulo 1000000007.

1<=n,m<=10000
1<=arr[i]<=800
Please pay attention to the memory limit of this problem(32M only)

Have you met this question in a real interview?  
Example
Givenn=3,m=2,arr=[1,2,3],return2
Explanation：

（0 means not taking this number）
0^0^0=0 X
0^0^3=3 √
0^2^0=2 X
0^2^3=1 X
1^0^0=1 X
1^0^3=2 X
1^2^0=3 √
1^2^3=0 X
There are 2 results that greater than m.
Givenn=3,m=0,arr=[1,1,1],return4
Explanation：

（0 means not taking this number）
0^0^0=0 X
0^0^1=1 √
0^1^0=1 √
0^1^1=0 X
1^0^0=1 √
1^0^1=0 X
1^1^0=0 X
1^1^1=1 √
There are 4 results that greater than m.
'''

class Solution:
    """
    @param n: The number of integers
    @param m: The lim of xor values
    @param arr: The integer values
    @return: Please calculate the number of xor values that greater than m ,and output the answer modulo 1000000007
    """
    def getAns(self, n, m, arr):
        # Write your code here
        if not arr:
            return 0
            
        # f[i][j] = number of xor combinations for the first i items whose result equals to j
        # we initialize the width to be 1023 max because thats the max with arr[x] < 800
        f = [ [0]*1024 for _ in range(2)]
        f[0][0] = 1 
        
        result = 0
        for i in range(1, n+1):
            for j in range(1024):
                f[i%2][j] = f[(i-1)%2][j] + f[(i-1)%2][j^arr[i-1]]
                
                if i == n and j > m:
                    result += f[i%2][j]
                    
        return result % 1000000007
        
        '''
        return self.helper(m, arr, 0, 0)
        '''
        '''
        result = 0
        for i in range(1, 2**n ):
            num = i 
            index = 0
            xor = 0
            while num:
                bit = num & 1 
                if bit:
                    xor ^= arr[index]
                num = num >> 1 
                index += 1 
            
            result += 1 if xor > m else 0 
        
        return result % 1000000007
                
        '''        
        
        '''
    def helper(self, m, arr, index, curr_xor):
        
        if index >= len(arr):
            return 1 if curr_xor > m else 0
            
        result = 1 if curr_xor > m else 0
        
        for i in range(index, len(arr)):
            num = arr[i]
            curr_xor ^= num
            result += self.helper(m, arr, i+1, curr_xor )
            curr_xor ^= num
        
        return result % 1000000007
        '''