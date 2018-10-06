class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0

        candies = [1] * len(ratings)

        # left to right
        for i, rating in enumerate(ratings):
            if i == 0:
                continue
            if rating > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # right to left
        ratings.reverse()
        candies.reverse()

        for i, rating in enumerate(ratings):
            if i == 0:
                continue
            if rating > ratings[i - 1]:
                candies[i] = max(candies[i], candies[i - 1] + 1)

        return sum(candies)


"""
left to right scan, and right to left scan
"""
