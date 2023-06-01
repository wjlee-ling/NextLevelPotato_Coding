"""
1631. Path With Minimum Effort
"""


from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        def dfs(y, x, visited, threadshold):
            if y == m - 1 and x == n - 1:
                return True  # Reach destination

            visited[y][x] = 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if not (0 <= ny < m and 0 <= nx < n and visited[ny][nx] == 0):
                    continue
                if abs(heights[ny][nx] - heights[y][x]) <= threadshold and dfs(ny, nx, visited, threadshold):
                    return True
            return False

        def canReachDestination(threadshold):
            visited = [[0] * n for _ in range(m)]
            return dfs(0, 0, visited, threadshold)

        left = 0
        ans = right = 10**6
        while left <= right:
            # 반올림과 버림의 차이?
            mid = left + (right - left) // 2
            if canReachDestination(mid):
                right = mid - 1  # Try to find better result on the left side
                ans = mid
            else:
                left = mid + 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    heights = [
        [[1, 2, 2], [3, 8, 2], [5, 3, 5]],
        [[1, 2, 3], [3, 8, 4], [5, 3, 5]],
        [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]],
    ]
    output = [2, 1, 0]

    for h in heights:
        print(solution.minimumEffortPath(h))
