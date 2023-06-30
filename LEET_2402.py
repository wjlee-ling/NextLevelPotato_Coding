"""
2402. Meeting Rooms III
"""


from collections import deque
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [0] * n
        used = [0] * n
        meetings = sorted(meetings)

        q = deque(meetings)
        # print(q)

        while q:
            start, end = q.popleft()
            # print(start, end, used)
            for i in range(n):
                if used[i] <= start:
                    rooms[i] += 1
                    used[i] = end
                    break
            else:
                fast = min(used)
                diff = fast - start
                q.appendleft([start + diff, end + diff])

        answer = 0
        most = 0
        for i in range(n):
            if most < rooms[i]:
                most = rooms[i]
                answer = i

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3]
    meetings = [[[0, 10], [1, 5], [2, 7], [3, 4]], [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]]
    output = [0, 1]
    for num, meeting in zip(nums, meetings):
        print("#", solution.mostBooked(num, meeting))
