"""
2517. Maximum Tastiness of Candy Basket
"""


from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            total, cnt = 0, 1
            for num in nums:
                if total + num <= mid:
                    total += num
                else:
                    total = num
                    cnt += 1
            if cnt > k:
                left = mid + 1
            else:
                right = mid
        return right


if __name__ == "__main__":
    solution = Solution()
    nums = [[7, 2, 5, 10, 8], [1, 2, 3, 4, 5]]
    ks = [2, 2]
    output = [18, 9]

    for n, k in zip(nums, ks):
        print(solution.splitArray(n, k))
