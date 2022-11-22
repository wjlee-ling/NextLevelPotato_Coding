# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
5 6 4
1 2
1 3
3 2
4 2
5 1
5 4
: -1

5 6 4
1 2
1 4
3 1
4 2
4 5
5 3
: 4
"""
# from collections import defaultdict

# N, M, K = map(int, input().split())
# graph = defaultdict(list)

# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# visited = [0] * (N + 1)
# answer = float("inf")


# def dfs(island, K, visit, visited):
#     global answer
#     for i in graph[island]:
#         if visited[i] == 0:
#             visited[i] = 1
#             # print("#: ", i, visit)
#             dfs(i, K, visit + 1, visited)

#             if i == K:
#                 answer = min(visit, answer)
#                 return


# dfs(K, K, 1, visited)
# if answer == float("inf"):
#     print(-1)
# else:
#     print(answer)

from collections import defaultdict, deque

N, M, K = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)
q = deque()
visited = [0] * (N + 1)

q.append(K)
visited[K] = 0
while q:
    island = q.popleft()
    for i in graph[island]:
        if visited[i] == 0:
            visited[i] = visited[island] + 1
            q.append(i)
        if i == K:
            break

if visited[K] == 0:
    print(-1)
else:
    print(visited[K])
