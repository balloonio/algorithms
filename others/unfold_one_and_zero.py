import collections


class Solution:
    def find(self, kth_row, nth_num):
        if not kth_row:
            # assert nth_num == 0
            return 0
        return self.traverse(0, kth_row, nth_num)

    def traverse(self, parent_val, kth_row, nth_num):
        if not kth_row:
            return parent_val
        # left sub tree
        if nth_num >= 0 and nth_num <= 2 ** (kth_row - 1) - 1:
            return self.traverse(parent_val, kth_row - 1, nth_num)
        # right sub tree
        else:
            return self.traverse(
                1 - parent_val, kth_row - 1, nth_num - 2 ** (kth_row - 1)
            )  # flip parent

    """
                                                                    0
                                                                   0 1
                                                                 0 1 1 0
                                                             0 1 1 0 1 0 0 1
                                                     0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0
                                     0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 1
     0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 1 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0
    """

    def testcase_reference(self, kth_row):
        if kth_row < 0:
            return
        queue = collections.deque()
        queue.append(0)
        row = 0

        while True:
            if row > kth_row:
                break
            level_size = 2 ** row
            level_str = " "
            for _ in range(level_size):
                val = queue.popleft()
                level_str += str(val) + " "
                queue.append(val)
                queue.append(1 - val)
            print(level_str.center(2 ** kth_row * 2 + 1))
            row += 1


sol = Solution()
print(sol.find(6, 15))
print(sol.testcase_reference(6))
