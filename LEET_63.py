# DP
# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        counts = [[0] * (C+1) for _ in range(R+1)]
        counts[0][0] = 1
        for r in range(R):
            for c in range(C):
 
                if obstacleGrid[r][c] == 1: # obstacle
                    continue
                else:
                    counts[r+1][c+1] = counts[r][c+1] + counts[r+1][c]
                
                if r+c == 0:
                    counts[1][1] = 1
                    
        return counts[R][C]