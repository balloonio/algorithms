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
