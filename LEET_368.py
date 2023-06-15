"""
368. Largest Divisible Subset
"""


from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        answer = []
        dp = []

        for num in nums:
            dp.append([num])
        # print(dp)

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    # print("#", dp[j], [nums[i]])
                    dp[i] = dp[j] + [nums[i]]
            # print("@", dp)

            if len(answer) < len(dp[i]):
                answer = dp[i]
            # print("@@", dp)

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [[1, 2, 3], [1, 2, 4, 8], [1, 2, 4, 8, 5]]
    output = [[1, 2], [1, 2, 4, 8], [1, 2, 4, 8]]

    for n in nums:
        print(solution.largestDivisibleSubset(n))
