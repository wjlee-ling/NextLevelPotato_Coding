"""
11. Container With Most Water
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0

        left, right = 0, len(height) - 1
        while left < right:
            answer = max(answer, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    height = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1]]
    output = [49, 1]

    for h in height:
        print("#", solution.maxArea(h))
