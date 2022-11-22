# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
7
5
1 4
3 5
7 6
1 5
4 3
: 4

5
5
1 3
2 3
3 4
4 5
4 2
: 5
"""
from collections import deque

N = int(input())
M = int(input())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

q = deque()
q.append(1)
visited = [0] * (N + 1)
visited[1] = 1
answer = 1

while q:
    friend = q.popleft()
    for i in range(1, N + 1):
        if graph[friend][i] == 1 and visited[i] == 0:
            visited[i] = 1
            answer += 1
            q.append(i)

print(answer)
