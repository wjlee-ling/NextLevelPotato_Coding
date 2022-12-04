# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
4 5
3 2 1 5
1 2 5
2 4 6
2 3 3
1 3 13
4 3 7
: 15

3 2
5 6 3
1 2 2
2 3 3
: -1

3 0
10 10 10
: -1

i -> j -> k 방으로 갈 수 있는지를 어떻게 체크해줘야 할까
"""

import sys
from heapq import *

input = sys.stdin.readline

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
D = [[10**18 for _ in range(10)] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

ans = -1
PQ = []
D[1][0] = 0
heappush(PQ, (D[1][0], 1, 0))
while PQ:
    cd, cur, prev = heappop(PQ)
    if cd > D[cur][prev]:
        continue
    if cur == N:
        ans = cd
        break
    for next, nd in G[cur]:
        if cd + nd >= D[next][cur % A[next]]:
            continue
        if cur != 1 and prev % A[cur] != next % A[cur]:
            continue
        D[next][cur % A[next]] = cd + nd
        heappush(PQ, (cd + nd, next, cur % A[next]))

print(ans)
