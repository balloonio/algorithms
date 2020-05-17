class Heap:
    """
    given father index = x
    left son index = 2*x + 1
    right son index = 2*x + 2
    """
    def __init__(self, nums):
        self.nums = nums
        
        lastsonidx = len(self.nums) - 1
        lastfatheridx = (lastsonidx-1) // 2
        for i in reversed(range(0, lastfatheridx + 1)):
            self.siftDown(i)
        
    # IMPORTANT, here we need siftUp not siftDown
    # in other words, a heap always need both siftUp and siftDown implementations
    def push(self, val):
        if not self.nums:
            self.nums += [val]
            return
        self.nums += [val]
        self.siftUp(len(self.nums)-1)
        
    def pop(self):
        if not self.nums:
            return None
        res = self.nums[0]
        self.nums[0] = self.nums[-1]
        self.nums.pop()
        self.siftDown(0)
        return res
        
    def siftUp(self, idx):
        if idx < 0 or idx >= len(self.nums):
            return
        n = len(self.nums)
        son = idx
        while son > 0:
            father = (son-1) //2
            if self.nums[father] <= self.nums[son]:
                return
            # need swap
            self.swap(father, son)
            son = father
        
    def siftDown(self, idx):
        if idx < 0 or idx >= len(self.nums):
            return
        father = idx
        n = len(self.nums)
        while father < len(self.nums):
            leftidx, rightidx = father*2 + 1, father*2 + 2
            if leftidx >=n and rightidx >= n:
                return
            smalleridx = leftidx
            if rightidx < n and self.nums[rightidx] < self.nums[smalleridx]:
                smalleridx = rightidx
                
            if self.nums[father] <= self.nums[smalleridx]:
                break
            
            # swap father and smaller
            self.swap(father, smalleridx)
            father = smalleridx
    
    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        
    def __len__(self):
        return len(self.nums)

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        define f[i] = min cost 
        4 
        9
        17
        """
        result = 0
        heap = Heap(sticks)
        
        while len(heap) > 1:
            min1, min2 = heap.pop(), heap.pop()
            result += min1 + min2
            heap.push(min1+min2)
            
        return result
            
