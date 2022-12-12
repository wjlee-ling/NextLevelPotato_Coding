"""
TC 22~24, 30 not solved.
"""

import sys
from collections import deque
sys.setrecursionlimit(10000000)

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    target = queue1 + queue2
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    summary = sum1+sum2

    if summary // 2 < max(target):
        return -1
    if abs(sum1-sum2) % 2 != 0:
        return -1

    def dfs(q1, q2, depth, sum1, sum2):
        if depth > 100000:
            return -1
        if sum1 == sum2:
            return depth
        elif sum1 > sum2:
            data = q1.popleft()
            q2.append(data)
            return dfs(q1, q2, depth+1, sum1-data, sum2+data)
        elif sum2 > sum1:
            data = q2.popleft()
            q1.append(data)
            return dfs(q1, q2, depth+1, sum1+data, sum2-data)
    answer = dfs(queue1, queue2, 0, sum1, sum2)
    return answer