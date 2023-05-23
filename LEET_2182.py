"""
2182. Construct String With Repeat Limit
"""
from collections import deque


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        answer = ""
        repeats = {}
        for c in sorted(s, reverse=True):
            repeats.setdefault(c, 0)
            repeats[c] += 1

        pq = deque()
        for key, value in repeats.items():
            pq.append([key, value])

        # print(pq)

        while pq:
            k1, v1 = pq.popleft()

            length = min(repeatLimit, v1)
            for _ in range(length):
                answer += k1

            k2 = ""
            v2 = 0
            if v1 - repeatLimit > 0:
                if pq:
                    k2, v2 = pq.popleft()
                else:
                    return answer

                answer += k2

                if v2 - 1 > 0:
                    pq.appendleft([k2, v2 - 1])
                pq.appendleft([k1, v1 - length])

        return answer


if __name__ == "__main__":
    solution = Solution()
    strings = ["cczazcc", "aababab"]
    repeatLimits = [3, 2]
    output = ["zzcccac", "bbabaa"]

    for s, r in zip(strings, repeatLimits):
        print(solution.repeatLimitedString(s, r))
