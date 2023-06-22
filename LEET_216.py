"""
216. Combination Sum III
"""


from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        visited = [0] * 10

        def recur(cnt, num, nums):
            if cnt == k:
                if sum(nums) == n:
                    # print("@", nums)
                    answer.append(nums)
                return

            visited[num] = 1
            for i in range(num + 1, 10):
                if visited[i] == 0:
                    nums.append(i)
                    recur(cnt + 1, i, nums[:])
                    nums.pop()
            visited[num] = 0

        for i in range(1, 10):
            visited[i] = 1
            recur(1, i, [i])
            visited[i] = 0

        return answer


if __name__ == "__main__":
    solution = Solution()
    ks = [3, 3, 4]
    ns = [7, 9, 1]
    output = [[[1, 2, 4]], [[1, 2, 6], [1, 3, 5], [2, 3, 4]], []]

    for k, n in zip(ks, ns):
        print("#", solution.combinationSum3(k, n))
