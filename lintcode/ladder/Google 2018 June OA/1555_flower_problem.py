""" 
Description
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Given a parameter m, and find the last day of m group flowering at the same time(each group has at least k plots)

If there isn't such day, output -1.

Example
input:
flowerded = [1,3,2]
k = 1
m = 2
output:
2

Input
[1,2,3,6,5,4,9,8,7]
2
2
Expected
8
"""

class Solution:
    """
    @param flowers: an array
    @param k: an integer
    @param m: an integer
    @return: the last day
    """
    def __init__(self):
        self.bloom_slot = set()
        self.slot2father = {}
        self.father_with_k_slots = set()
        self.father2slots = {}

    def flowerProblem(self, flowers, k, m):
        # Write your code here
        if not flowers:
            return -1

        result = -1
        for day, slot in enumerate(flowers):
            if slot not in self.slot2father:
                self.slot2father[slot] = slot
                self.father2slots[slot] = 1
                self.bloom_slot.add(slot)
                if k == 1:
                    self.father_with_k_slots.add(slot)

            if slot-1 in self.bloom_slot:
                self.union(slot, slot-1, k)
            if slot+1 in self.bloom_slot:
                self.union(slot, slot+1, k)

            if len(self.father_with_k_slots) >= m:
                result = max(day + 1, result)

        return result

    def union(self, slot1, slot2, k):
        father1 = self.find(slot1)
        father2 = self.find(slot2)

        if father1 == father2:
            return

        self.slot2father[father1] = father2
        self.father2slots[father2] += self.father2slots[father1]
        self.father2slots.pop(father1)
        if self.father2slots[father2] >= k:
            self.father_with_k_slots.add(father2)
        if father1 in self.father_with_k_slots:
            self.father_with_k_slots.remove(father1)

    def find(self, slot):
        path = []
        while slot != self.slot2father[slot]:
            path += [slot]
            slot = self.slot2father[slot]

        for p in path:
            self.slot2father[p] = slot
        return slot
