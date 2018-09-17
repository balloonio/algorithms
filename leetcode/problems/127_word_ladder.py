class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dict = self.build_dict(wordList)
        if endWord not in dict:
            return 0

        q = collections.deque()
        visited = set()
        q.append( (beginWord, 1) )
        visited.add(beginWord)

        while q:
            word, step = q.popleft()
            trans = self.get_all_trans(word)
            for transform in trans:
                if transform not in dict:
                    continue
                if transform in visited:
                    continue
                if transform == endWord:
                    return step + 1
                q.append( (transform, step+1) )
                visited.add(transform)
        return 0


    def get_all_trans(self, word):
        trans = []
        for i, c in enumerate(word):
            for nc in 'abcdefghijklmnopqrstuvwxyz':
                if c == nc:
                    continue
                nw = word[:i] + nc + word[i+1:]
                trans.append(nw)
        return trans

    def build_dict(self, words):
        dict = set()
        for word in words:
            dict.add(word)
        return dict

# be careful with queue popleft() not pop()
# also be careful with step increment
