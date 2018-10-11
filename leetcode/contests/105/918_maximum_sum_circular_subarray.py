class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        k = len(A)
        doublea = A + A
        ps = [0]  # prefix sum
        for num in doublea:
            ps.append(ps[-1] + num)

        maxsum = -math.inf
        ascdeq = collections.deque()  # [ (prefix sum, index of the prefix sum) ]
        for i, presum in enumerate(ps):
            # 双端队列 端口操作 while loop疯狂pop 维护端口
            while ascdeq and ascdeq[-1][0] >= presum:
                maxsum = max(maxsum, presum - ascdeq[-1][0])
                ascdeq.pop()
            # 至此 双端队列 严格递增 并且保持元素入列时间的单调性
            # 如果 双端队列 while loop疯狂popleft 维护端尾
            # 尾端元素 距离当前ps已经超过k个距离 意味着环装数组已经套圈 不可取
            while ascdeq and i - ascdeq[0][1] > k:
                ascdeq.popleft()
            # 双端队列 端尾取值操作
            if ascdeq:
                maxsum = max(maxsum, presum - ascdeq[0][0])
            # 记得将元素入列
            ascdeq.append((presum, i))
        return maxsum


"""
特别注意两个地方
L31 第一次提交漏掉了 忘记入列
L20 第二次提交漏掉了 这里因为是数组最大和 所以就算pop的比自己大 就算是负数 也要看能不能update maxsum
总结
1. while循环维护deque端口 这里通常要不停pop 注意pop之前是不是要做些什么
2. while循环维护deque端尾 这里通常也是根据某些条件pop 注意pop之前是不是要做些什么
3. 端尾取值操作 是否可以update最大值或者是结果等变量
4. 这个时候记得把元素放入双端队列
这道题和 1616_shortest_subarray_ii 超级像, 一定对比来看
"""

"""
话还没说满 lc上去看了下别人的速度 才发现还有更快的解法..连额外空间都不需要
"""


class Solution:  # noqa: F811
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxSum, minSum = float("-inf"), float("inf")
        curMax, curMin = 0, 0
        total = 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return maxSum if maxSum < 0 else max(maxSum, total - minSum)


"""
靠..总算看明白了下面这个
解决环形类问题的关键有两个
1.直接暴力数组x2一下 就像我上面做的那个solution
2.看看能不能做一个 "极" 的转化
比如说这道题, 最大子数组要么是连在一起出现在A0到An-1之间
要么是套环 从A0到Ai 然后中间断开 再从Aj到An-1 相当于从Aj到Ai
那这个时候其实就是要在A0到An-1之间找一个最小子数组, 这样剩下两边的数就最大了
"""


class Solution:  # noqa: F811
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_ending_here = 0
        max_so_far = 0

        for item in A:
            max_ending_here += item
            if max_ending_here <= 0:
                max_ending_here = 0
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

        if max_so_far == 0:
            return max(A)

        min_ending_here = 0
        min_so_far = 0

        for item in A:
            min_ending_here += item
            if min_ending_here >= 0:
                min_ending_here = 0
            if min_so_far > min_ending_here:
                min_so_far = min_ending_here

        return max(max_so_far, sum(A) - min_so_far)
