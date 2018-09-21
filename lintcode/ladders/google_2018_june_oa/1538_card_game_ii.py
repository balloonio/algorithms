""" 
Description
You are playing a card game with your friends, there are n cards in total. Each card costs cost[i] and inflicts damage[i] damage to the opponent. You have a total of totalMoney dollars and need to inflict at least totalDamage damage to win. And Each card can only be used once. Determine if you can win the game.

Have you met this question in a real interview?  
Example
input:
cost = [1,2,3,4,5]
damage = [1,2,3,4,5]
totalMoney = 10
totalDamage = 10

output:
true
"""


class Solution:
    """
    @param cost: costs of all cards
    @param damage: damage of all cards
    @param totalMoney: total of money
    @param totalDamage: the damage you need to inflict
    @return: Determine if you can win the game
    """

    def cardGame(self, cost, damage, totalMoney, totalDamage):
        # Write your code here
        if not cost:
            return False

        f = [[0] * (totalMoney + 1) for first_i_cards in range(2)]

        for i in range(len(f[0])):
            f[0][i] = 0

        now, old = 0, 1

        for ith in range(len(cost)):
            now, old = old, now
            for m in range(len(f[now])):
                c = cost[ith]
                dmg_if_ith_card_not_picked = f[old][m]
                dmg_if_ith_card_picked = (
                    f[old][m - c] + damage[ith] if m - c >= 0 else -math.inf
                )
                f[now][m] = max(dmg_if_ith_card_picked, dmg_if_ith_card_not_picked)
                if f[now][m] >= totalDamage:
                    return True
        # print(f)
        return False
