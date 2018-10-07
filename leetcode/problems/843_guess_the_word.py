# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """


class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """

        candidates = set(wordlist)
        LIMIT = 10

        for i in range(LIMIT):
            if not candidates:
                break
            guess = candidates.pop()
            match = master.guess(guess)
            candidates = self.update_candidates(guess, match, candidates)

    def update_candidates(self, word, reqmatch, candidates):
        new_candidates = set()
        for cand in candidates:
            matched = self.get_match(word, cand)
            if matched == reqmatch:
                new_candidates.add(cand)
        return new_candidates

    def get_match(self, source, target):
        PASSLEN = 6
        match = 0
        for i in range(PASSLEN):
            match += source[i] == target[i]
        return match


"""
logical approach: we limit the scope of candidates everytime we make a new guess
"""
