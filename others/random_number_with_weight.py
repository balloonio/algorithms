"""
是给一堆数字每个都有weight，根据weight random输出数字

example
stdin input: (first row number, second row weight)
100 123 -10 9 5.6
1   1   1   1 4

"""

import sys
import random

nums = []
weights = []
for i, line in enumerate(sys.stdin):
    if i == 0:
        nums = [float(number) for number in line.strip("\n").split()]
    else:
        weights = [float(w) for w in line.strip("\n").split()]

if not nums or not weights or len(nums) != len(weights):
    raise ValueError("Input is not valid")


def find_random_with_weight(nums, weights):
    totalsum = sum(weights)
    randnum = random.randint(1, totalsum)

    cumsum = 0
    for i, w in enumerate(weights):
        cumsum += w
        if cumsum >= randnum:
            return nums[i]


print(find_random_with_weight(nums, weights))
