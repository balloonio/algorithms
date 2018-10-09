# This DFS solution is nice simple easy brutal, but takes too long even with pruning
class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        if not quality:
            return 0
        if K > len(quality):
            return -1  # error

        wage_qua = list(zip(wage, quality))
        wage_qua.sort()
        wage = [wq[0] for wq in wage_qua]
        quality = [wq[1] for wq in wage_qua]

        self.min_payment = math.inf
        self.dfs(quality, wage, 0, K, set(), 0)
        return self.min_payment

    # dfs to pick k different workers from all the workers
    def dfs(self, quality, wage, idx, k, selected, selected_minwage):
        if selected_minwage >= self.min_payment:
            return
        # already found k workers
        if len(selected) == k:
            self.update_minimum_payment(quality, wage, selected, selected_minwage)
            return
        # pick the next worker from worker[idx:]
        n = len(quality)
        for i in range(idx, n):
            # pruning if not enough workers left
            if n - i + len(selected) < k:
                break
            selected.add(i)
            self.dfs(quality, wage, i + 1, k, selected, selected_minwage + wage[i])
            selected.remove(i)
        return

    # get the minimum payment based on the current worker selection
    def update_minimum_payment(self, quality, wage, selected, payment):
        # the minimum possible payment would be the sum of all their min wage
        total_qual = sum([quality[i] for i in selected])
        max_raise_ratio = 1
        # but this payment might not meet the min wage after divide by quality ratio
        for i in selected:
            allocated = payment * quality[i] / total_qual
            # if satisfied min wage, ignore him, go check next worker
            if allocated >= wage[i]:
                continue
            max_raise_ratio = max(max_raise_ratio, wage[i] / allocated)

        payment *= max_raise_ratio
        self.min_payment = min(self.min_payment, payment)


# 这道题思路有点巧妙.. 自己没能想到 看答案的. 总结一下 重点有3个
# 1. 取最小总工资的方案的时候 一定有一个人的工资是最低工资, 不然的话我们还可以进一步压低总工资
# 2. 当这个人i工人取最低工资的时候 总工资和总质量的比是可以算出来的 因为 Qi/Qtotal *Wtotal = Wi
#    所以 Wi/Qi = Wtotal/Qtotal ,所以这个时候我们希望剩下的Qtotal最小来达到Wtotal最小
# 3. 如何确定哪一个工人可以成为这个拿最低工资的工人呢? 这里需要一点intuition
#    假设我们选了k个工人,拿最低工资的那个一定是 Wi/Qi最大的.
#    我们不妨从反方向思考试着理解 如果一个工人i他的Wi是无穷小 Qi是无穷大,那他是不可能成为这个短板的
#    因为他做了将近百分百的活 却只要求几乎零的工资 一定是k个工人里的其他人无法满足自己的最低工资而抱怨
#    所以这个短板将会出现在Wi/Qi最大的那个工人身上
class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        if not quality:
            return 0
        if K > len(quality):
            return -1  # error

        wage_qua = list(zip(wage, quality))
        wage_qua.sort(key=lambda wq: wq[0] / wq[1])  # sort by wage / quality
        maxheap = []
        qtotal = 0
        result = math.inf

        for w, q in wage_qua:
            ratio = w / q
            qtotal += q
            heapq.heappush(maxheap, -q)

            # remove the highest quality worker from the heap and from qtotal
            if len(maxheap) > K:
                qtotal += heapq.heappop(maxheap)
            # the current worker is the shortest wood in the bucket
            # because he has the largest ratio so far
            if len(maxheap) == K:
                result = min(result, ratio * qtotal)
        return result
