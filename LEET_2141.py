"""
2141. Maximum Running Time of N Computers
"""


from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n
        print(left, right)
        while left < right:
            target = right - ((right - left) // 2)

            extra = 0
            for power in batteries:
                extra += min(power, target)

            if extra // n >= target:
                left = target
            else:
                right = target - 1

            print(left, right, target)

        return left


if __name__ == "__main__":
    solution = Solution()
    ns = [2, 2]
    batteries = [[3, 3, 3], [1, 1, 1, 1]]
    output = [4, 2]

    for n, b in zip(ns, batteries):
        print(solution.maxRunTime(n, b))
