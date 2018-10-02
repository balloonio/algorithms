class TrieNode:
    def __init__(self):
        self.next = {} # next char to next node 
        self.is_word = False 

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root 
        for c in word:
            if c not in node.next:
                node.next[c] = TrieNode()
            node = node.next[c]
        node.is_word = True 

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root 
        for c in word:
            if c not in node.next:
                return False
            node = node.next[c]
        return node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root 
        for c in prefix:
            if c not in node.next:
                return False 
            node = node.next[c]
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)