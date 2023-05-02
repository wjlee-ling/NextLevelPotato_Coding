"""
1406. Stone Game III
"""


from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = float("-inf")
            take = 0
            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                dp[i] = max(dp[i], take - dp[j + 1])
            print(dp)

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"


if __name__ == "__main__":
    solution = Solution()
    # values = [[1, 2, 3, 7], [1, 2, 3, -9], [1, 2, 3, 6], [-2], [-1, -2, -3]]
    values = [[1, 2, 3, -9]]
    output = ["Bob", "Alice", "Tie", "Bob", "Tie"]

    for v in values:
        print(solution.stoneGameIII(v))
