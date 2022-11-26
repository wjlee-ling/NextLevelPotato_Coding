# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import heapq


def solution():
    global answer
    answer = 0
    N, K = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u][v] = graph[v][u] = 1
    cities = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)

    def dfs(city: int, graph: list, cities: list, visited: list, route: list, trash: int, N: int, K: int):
        global answer
        for i in range(1, N + 1):
            if graph[city][i] == 1 and visited[i] == 0:
                visited[i] = 1
                heapq.heappush(route, cities[i])
                trash += cities[i]
                while trash > K:
                    trash -= route.pop(0)
                answer = max(answer, trash)
                dfs(i, graph, cities, visited, route, trash, N, K)
                visited[i] = 0

        return

    dfs(1, graph, cities, visited, [], 0, N, K)

    return answer


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

21번 시간초과
이외 다수 runtime error, 오답
"""
