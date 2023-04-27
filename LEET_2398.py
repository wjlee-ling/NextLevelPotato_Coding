from collections import deque
from typing import List


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        answer = 0
        left = 0
        curr = 0
        q = deque()

        n = len(chargeTimes)
        for right in range(n):
            while q and chargeTimes[q[-1]] <= chargeTimes[right]:
                q.pop()
            q.append(right)
            curr += runningCosts[right]

            while q and chargeTimes[q[0]] + (right - left + 1) * curr > budget:
                if q[0] == left:
                    q.popleft()
                curr -= runningCosts[left]
                left += 1
            answer = max(answer, right - left + 1)

        return answer


if __name__ == "__main__":
    solution = Solution()
    chargeTimes = [[3, 6, 1, 3, 4], [11, 12, 19]]
    runningCosts = [[2, 1, 3, 4, 5], [10, 8, 7]]
    budget = [25, 19]

    for c, r, b in zip(chargeTimes, runningCosts, budget):
        print(solution.maximumRobots(c, r, b))
