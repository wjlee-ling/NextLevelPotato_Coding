from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        answer = 2
        n = len(nums)
        dp = [[2] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                for k in range(i):
                    if nums[k] + diff == nums[i]:
                        dp[i][j] = max(dp[i][j], dp[k][i] + 1)
                        break

                answer = max(answer, dp[i][j])
            # print(dp)

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [[3, 6, 9, 12], [9, 4, 7, 2, 10], [20, 1, 15, 3, 10, 5, 8]]
    output = [4, 3, 4]

    for num in nums:
        print(solution.longestArithSeqLength(num))
