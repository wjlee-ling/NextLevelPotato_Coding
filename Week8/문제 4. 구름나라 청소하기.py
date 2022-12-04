# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
solved
"""
import sys

sys.setrecursionlimit(1234)


def solution():
    global K
    N, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    cities = [0] + list(map(int, input().split()))
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    answer = [0] * (K + 1)

    def dfs(cur: int, prev: int):
        global K
        for i in range(K + 1):
            if not dp[prev][i]:
                continue

            answer[i] = dp[cur][i] = 1
            if i + cities[cur] <= K:
                answer[i + cities[cur]] = dp[cur][i + cities[cur]] = 1
        print(dp)
        print(answer)
        for next in graph[cur]:
            if next == prev:
                continue
            dfs(next, cur)

    dp[0][0] = 1
    dfs(1, 0)

    for i in range(K, -1, -1):
        if answer[i]:
            return i


if __name__ == "__main__":
    print(solution())


"""
4 9
1 2
2 3
2 4
3 7 4 5
: 8

5 8
1 2
2 3
3 4
3 5
2 1 4 2 1
: 8
"""
