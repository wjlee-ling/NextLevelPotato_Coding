from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1  # edge case

        def check(day):
            """주어진 day 값에 m개의 부케를 만들 수 있다면 True 반환"""
            temp_m, temp_k = m, k
            print(temp_m, temp_k)
            for x in bloomDay:
                if x <= day:
                    temp_k = temp_k - 1
                else:
                    temp_k = k
                if temp_k == 0:
                    temp_m = temp_m - 1
                    temp_k = k
                if temp_m == 0:
                    return True
            return False

        # binary search
        left, right = 0, max(bloomDay)
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    solution = Solution()
    bloomDays = [[1, 10, 3, 10, 2], [1, 10, 3, 10, 2], [7, 7, 7, 7, 12, 7, 7], [1000000000, 1000000000]]
    m = [3, 3, 2, 1]
    k = [1, 2, 3, 1]

    for a, b, c in zip(bloomDays, m, k):
        print(solution.minDays(a, b, c))
