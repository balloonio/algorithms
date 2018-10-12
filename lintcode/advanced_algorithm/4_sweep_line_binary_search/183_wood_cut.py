class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0

        min_piece = 1
        max_piece = max(L)

        start, end = min_piece, max_piece
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_possible(mid, L, k):
                start = mid
            else:
                end = mid

        if self.is_possible(end, L, k):
            return end
        if self.is_possible(start, L, k):
            return start
        return 0

    def is_possible(self, piece_length, L, k):
        piece_number = 0
        for length in L:
            piece_number += length // piece_length

        return piece_number >= k
