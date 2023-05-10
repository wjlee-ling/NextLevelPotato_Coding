"""
474. Ones and Zeroes
"""

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
            print(dp)

        return dp[m][n]


if __name__ == "__main__":
    solution = Solution()
    strs = [["10", "0001", "111001", "1", "0"], ["10", "0", "1"], ["111", "1000", "1000", "1000"]]
    m = [5, 1, 9]
    n = [3, 1, 3]
    output = [4, 2, 3]

    for s, m1, n1 in zip(strs, m, n):
        print(solution.findMaxForm(s, m1, n1))
