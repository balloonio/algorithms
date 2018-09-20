import copy


class Trie:
    def __init__(self):
        self.root = TrieNode()


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Solution:
    """
    @param: board: a list of lists of character
    @param: words: a list of string
    @return: an integer
    """

    def __init__(self):
        self.max_wcnt = 0
        self.trie = None
        self.board = None
        self.h, self.w = 0, 0

    def boggleGame(self, board, words):
        # write your code here
        if not board or not board[0]:
            return 0

        self.board = board
        self.h, self.w = len(self.board), len(self.board[0])
        self.trie = self.build_trie(words)
        empties = [[True] * self.w for _ in range(self.h)]
        self.helper(0, 0, empties, 0)
        return self.max_wcnt

    def helper(self, startx, starty, empties, wcnt):
        self.max_wcnt = max(self.max_wcnt, wcnt)
        for x in range(startx, self.h):
            for y in range(starty, self.w):
                if not empties[x][y]:
                    continue
                for word_path in self.viable_words_at(x, y, empties):
                    for used_slot in word_path:
                        empties[used_slot[0]][used_slot[1]] = False
                    self.helper(x, y, empties, wcnt + 1)
                    for used_slot in word_path:
                        empties[used_slot[0]][used_slot[1]] = True
            starty = 0
        return

    def viable_words_at(self, x, y, empties):
        node = self.trie.root
        begin_char = self.board[x][y]
        if begin_char not in node.children:
            return []
        node = node.children[begin_char]
        picked = [(x, y)]
        empties[x][y] = False
        picked_word_paths = []
        self.helper2(x, y, node, empties, picked, picked_word_paths)
        empties[x][y] = True
        return picked_word_paths

    # all the nearby char should be in node.children to qualify search
    def helper2(self, x, y, node, empties, picked, picked_word_paths):
        if node.is_word:
            picked_word_paths.append(picked[:])
            return
        for nearby in self.get_nearby_empty(x, y, empties):
            nx, ny = nearby
            nchar = self.board[nx][ny]
            if nchar not in node.children:
                continue
            next_node = node.children[nchar]
            picked.append((nx, ny))
            empties[nx][ny] = False
            self.helper2(nx, ny, next_node, empties, picked, picked_word_paths)
            picked.pop()
            empties[nx][ny] = True

    def get_nearby_empty(self, x, y, empties):
        for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= self.h or ny < 0 or ny >= self.w:
                continue
            if empties[nx][ny]:
                yield (nx, ny)

    def build_trie(self, words):
        trie = Trie()
        for word in words:
            self.add_to_trie(trie, word)
        return trie

    def add_to_trie(self, trie, word):
        node = trie.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True


# This problem has 2 very sneaky DFS performance trap
# 1. L36 L37 L46 Normally, or intuitively, at each helper() DFS level, I would loop through all the empty slots left on board.
#     But here, you only need to do DFS when you see an empty slot while you are exploring towards the bottom part
#     of the board. Any empty slot on the top part of the board must have been already explored with previous DFS
# 2. L66 The return is needed here. Let's say we can pick 'a' and 'aaaa' here at (0,0). Which one shall we pick? We pick 'a'.
#    Plus, we don't even need to explore 'aaaa' at all. Why? Because we can always pick more words or same words when we put 'a'
#    at this slot rather than 'aaaa'
