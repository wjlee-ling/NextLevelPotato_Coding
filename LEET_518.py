"""
518. Coin Change II
"""


from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 1

        for i in range(1, len(coins) + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
                # print(dp)

        return dp[len(coins)][amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [0] * (amount + 1)
#         dp[0] = 1

#         for coin in coins:
#             for i in range(coin, amount + 1):
#                 dp[i] += dp[i - coin]

#         print(dp)

#         return dp[amount]


if __name__ == "__main__":
    solution = Solution()
    amounts = [5, 3, 10]
    coins = [[1, 2, 5], [2], [10]]
    output = [4, 0, 1]

    for amount, coin in zip(amounts, coins):
        print(solution.change(amount, coin))
