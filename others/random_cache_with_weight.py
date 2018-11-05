# design a data structure to hold objects with a corresponding integer weight. It should support:
# Obtain an object randomly with probability equal to (weight of the element) / (sum of the weights).
# Set an object-weight pair. If the object is already in the structure, its weight will be updated.
# Otherwise, the object will be inserted and set to its weight. If the weight is zero, the object can be removed.
import random


class Node:
    def __init__(self, key, weight):
        self.key = key  # object key or id
        self.weight = weight
        self.prev = None
        self.nxt = None


class NodeList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def delete(self, node):
        self.size -= 1

        if self.head == node:
            self.head = node.nxt
        if self.tail == node:
            self.tail = node.prev

        if node.prev is not None:
            node.prev.nxt = node.nxt
        if node.nxt is not None:
            node.nxt.prev = node.prev

    def insert(self, node):
        self.size += 1

        # blank list
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return

        # something in there
        node.prev = self.tail
        self.tail.nxt = node
        self.tail = node


class WeightRandom:
    def __init__(self):
        self.key2node = {}  # object key or id : the node contains the object info (weight, id)
        self.nodelist = NodeList()
        self.totalsum = 0

    # O(1)
    def setObjectWeight(self, obj_key, weight):
        # not in map and also try to zero weight, no op
        if weight == 0 and obj_key not in self.key2node:
            return
        # not in map, insert node
        if obj_key not in self.key2node:
            node = Node(obj_key, weight)
            self.key2node[obj_key] = node
            self.nodelist.insert(node)
            self.totalsum += weight
        # in map, update
        else:
            self.totalsum += weight - self.key2node[obj_key].weight
            self.key2node[obj_key].weight = weight

            # if weight is zero, try to remove
            if weight == 0:
                self.nodelist.delete(self.key2node[obj_key])
                self.key2node.pop(obj_key)

    # linear O(n)
    def getRandom(self):
        if self.totalsum == 0:
            return None

        randres = random.randint(1, self.totalsum)
        # loop through lsit to find the first node that is greater than or equal to randres
        cumsum = 0
        node = self.nodelist.head

        while node is not None:
            cumsum += node.weight
            if cumsum >= randres:
                return node.key  # obj key
            node = node.nxt

        return None


wr = WeightRandom()
wr.setObjectWeight(1, 1)
wr.setObjectWeight(2, 1)
wr.setObjectWeight(2, 0)
wr.setObjectWeight(3, 2)

for i in range(10):
    print(wr.getRandom())
