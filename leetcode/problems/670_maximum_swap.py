class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return num

        numstr = str(num)
        heap = []
        removed = set()

        for i, c in enumerate(numstr):
            digit = int(c)
            heap.append((-digit, -i))
        heapq.heapify(heap)

        resultstr = ""
        for i, c in enumerate(numstr):
            digit = int(c)
            if digit == self.top_digit(heap, removed):
                removed.add((-digit, -i))
                continue
            digit, idx = self.heap_pop(heap, removed)
            return int(
                numstr[:i]
                + numstr[idx]
                + numstr[i + 1 : idx]
                + numstr[i]
                + numstr[idx + 1 :]
            )
        return num

    def clean_top(self, heap, removed):
        while heap and heap[0] in removed:
            heapq.heappop(heap)

    def top_digit(self, heap, removed):
        self.clean_top(heap, removed)
        if not heap:
            return None
        return -heap[0][0]

    def heap_pop(self, heap, removed):
        self.clean_top(heap, removed)
        if not heap:
            return None, None
        neg_digit, neg_idx = heapq.heappop(heap)
        return -neg_digit, -neg_idx


# The best approach to use set+heap for hashheap is to use set and clean_top
# before top and pop, reference skyline problem
