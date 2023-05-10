"""
1027. Longest Arithmetic Subsequence
"""


from typing import List


class Solution:
    def longestArithSeqLength(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())


if __name__ == "__main__":
    solution = Solution()
    nums = [[3, 6, 9, 12], [9, 4, 7, 2, 10], [20, 1, 15, 3, 10, 5, 8]]
    output = [4, 3, 4]

    for num in nums:
        print(solution.longestArithSeqLength(num))
