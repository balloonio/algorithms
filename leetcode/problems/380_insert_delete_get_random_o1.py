class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val2idx = {}
        self.values = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val2idx:
            return False
        self.val2idx[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val2idx:
            return False

        idx = self.val2idx[val]
        self.val2idx.pop(val)
        mv_val = self.values[-1]
        if mv_val == val:
            self.values.pop()
            return True
        self.values[idx] = mv_val
        self.val2idx[mv_val] = idx
        self.values.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.values:
            return None
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
