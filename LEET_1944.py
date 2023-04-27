from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack:
                answer[i] += 1
                if heights[i] > stack[-1]:
                    stack.pop()
                else:
                    break

            stack.append(heights[i])
            # print(stack, heights[i], answer)

        return answer


if __name__ == "__main__":
    solution = Solution()
    heights = [[10, 6, 8, 5, 11, 9], [5, 1, 2, 3, 10]]
    output = [[3, 1, 2, 1, 1, 0], [4, 1, 1, 1, 0]]

    for h in heights:
        print(solution.canSeePersonsCount(h))
