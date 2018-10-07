class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        if not words:
            return []

        plen = len(pattern)
        result = []
        for word in words:
            if len(word) != plen:
                continue
            if self.pattern_match(word, pattern):
                result += [word]
        return result

    def pattern_match(self, word, pattern):
        mapping = {}  # word char : pattern char
        used_pc = set()  # used pattern char

        for i, wc in enumerate(word):
            pc = pattern[i]
            if wc not in mapping:
                if pc in used_pc:
                    return False
                else:
                    mapping[wc] = pc
                    used_pc.add(pc)
            else:
                if pc != mapping[wc]:
                    return False
        return True


"""
for each word, loop through word and try to build mapping against pattern and compare
1. If char in word not in mapping, try to build mapping.
If it fails, ( the pattern char being mapped to is already used ), then this word fails
2. If char in word is in mapping, try to compare the char in pattern with the supposed
mapped pattern char in mapping. If fails, this word fails
"""
