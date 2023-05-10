"""
2251. Number of Flowers in Full Bloom
"""


from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def fullBloomFlowers(self, A: List[List[int]], persons: List[int]) -> List[int]:
        start, end = sorted(a for a, b in A), sorted(b for a, b in A)
        # print("@", start)
        # print("#", end)
        return [bisect_right(start, t) - bisect_left(end, t) for t in persons]


if __name__ == "__main__":
    solution = Solution()
    flowers = [[[1, 6], [3, 7], [9, 12], [4, 13]], [[1, 10], [3, 3]]]
    people = [[2, 3, 7, 11], [3, 3, 2]]
    output = [[1, 2, 2, 2], [2, 2, 1]]

    for f, p in zip(flowers, people):
        print(solution.fullBloomFlowers(f, p))
