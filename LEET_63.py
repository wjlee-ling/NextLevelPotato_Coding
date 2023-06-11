"""
63. Unique Paths II
"""


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N = len(obstacleGrid)
        M = len(obstacleGrid[0])
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        dp[1][1] = 1

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    continue
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

        # for d in dp:
        #     print(d)
        # print()

        if obstacleGrid[0][0] == 1:
            return 0

        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    obstacleGrids = [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 1], [0, 0]], [[0, 1]], [[1]], [[0, 0]]]
    output = [2, 1, 0, 0, 1]
    for grid in obstacleGrids:
        print(solution.uniquePathsWithObstacles(grid))
