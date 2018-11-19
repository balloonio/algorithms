import unittest
import random
import threading


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prv = None
        self.nxt = None


class NodeList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if not node:
            return

        if not self.head:
            self.head = node
            self.tail = node
            return

        node.nxt = self.head
        self.head.prv = node
        self.head = node

    def remove(self, node):
        if not node:
            return

        if self.head is node:
            self.head = node.nxt
        if self.tail is node:
            self.tail = node.prv

        if node.prv is not None:
            node.prv.nxt = node.nxt
        if node.nxt is not None:
            node.nxt.prv = node.prv

        node.nxt = None
        node.prv = None


class LRUcache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key2node = {}
        self.nodelist = NodeList()
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            if key not in self.key2node:
                return None
            node = self.key2node[key]
            self.nodelist.remove(node)
            self.nodelist.insert(node)
            return node.val

    def put(self, key, val):
        with self.lock:
            if self.capacity == 0:
                return

            if key in self.key2node:
                node = self.key2node[key]
                node.val = val
                self.nodelist.remove(node)
                self.nodelist.insert(node)
                return

            if len(self.key2node) == self.capacity:
                node2remove = self.nodelist.tail
                self.key2node.pop(node2remove.key)
                self.nodelist.remove(node2remove)

            node = Node(key, val)
            self.key2node[key] = node
            self.nodelist.insert(node)


class LruTest(unittest.TestCase):
    def test_empty(self):
        cache = LRUcache(0)
        self.assertIsNone(cache.get("key0"))

    def test_singleitem(self):
        cache = LRUcache(1)
        cache.put("key0", "val0")
        self.assertEqual(cache.get("key0"), "val0")

    def test_evict(self):
        cache = LRUcache(1)
        cache.put("key0", "val0")
        cache.put("key1", "val1")
        self.assertIsNone(cache.get("key0"))
        self.assertEqual(cache.get("key1"), "val1")

    def test_bigput(self):
        size = random.randint(100, 1000)
        gensize = size * 5
        control = [None] * size
        cache = LRUcache(size)
        for i in range(gensize):
            randkey = random.random() * 1000
            randval = random.random() * 100
            cache.put(randkey, randval)
            control[i % size] = (randkey, randval)

        for key, val in control:
            self.assertEqual(cache.get(key), val)


if __name__ == "__main__":
    unittest.main()
