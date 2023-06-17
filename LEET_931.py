"""
931. Minimum Falling Path Sum
"""


from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m]
        dp.extend(matrix)

        # for mat in matrix:
        #     print(mat)
        # print()

        dx = [-1, 0, 1]

        def is_valid(y, x):
            if 0 <= y < n and 0 <= x < m:
                return True
            return False

        for y in range(len(dp) - 1 - 1, -1, -1):
            for x in range(len(dp[0]) - 1, -1, -1):
                temp = float("inf")
                for i in range(3):
                    nx = x + dx[i]
                    if is_valid(y, nx):
                        temp = min(matrix[y][nx], temp)
                dp[y][x] += temp

        # for d in dp:
        #     print(d)
        # print()

        return min(matrix[0])


if __name__ == "__main__":
    solution = Solution()
    matrices = [
        [[2, 1, 3], [6, 5, 4], [7, 8, 9]],
        [[-19, 57], [-40, -5]],
    ]
    output = [13, -59]

    for m in matrices:
        print("#", solution.minFallingPathSum(m))
