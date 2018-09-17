class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return [[]]

        dict = collections.defaultdict(list)
        for word in strs:
            hash = self.get_hash(word)
            dict[hash].append(word)

        result = []
        for hash, words in dict.items():
            result.append(words)
        return result

    def get_hash(self, word):
        hash = [0]*26
        for c in word:
            hash[ord(c)-ord('a')] += 1
        return tuple(hash)

# remember list is not hashable but mutable
#          tuple is hashable but immutable
