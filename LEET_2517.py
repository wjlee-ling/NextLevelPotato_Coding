"""
2517. Maximum Tastiness of Candy Basket
"""


from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        print(price)

        left = 0
        right = price[-1] - price[0]

        while left - right:
            mid = (left + right + 1) // 2
            cnt = 1

            j = 0
            for i in range(1, len(price)):
                if price[i] - price[j] >= mid:
                    cnt += 1
                    j = i

            if cnt >= k:
                left = mid
            else:
                right = mid - 1

            print(left, right, mid)

        return left


if __name__ == "__main__":
    solution = Solution()
    prices = [[13, 5, 1, 8, 21, 2], [1, 3, 1], [7, 7, 7, 7]]
    ks = [3, 2, 2]
    output = [0, 2, 0]

    for p, k in zip(prices, ks):
        print(solution.maximumTastiness(p, k))
