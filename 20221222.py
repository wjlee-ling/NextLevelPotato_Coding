"""
프로그래머스 - 합승 택시 요금 (https://school.programmers.co.kr/learn/courses/30/lessons/72413)

solved
"""

import heapq


def solution(n, s, a, b, fares):
    ans = float("inf")
    graph = [[] for _ in range(n + 1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))
    print(graph)

    distances = [[]]
    for i in range(1, n + 1):
        distances.append(dijkstra(i, graph, n))
    print(distances)

    for i in range(1, n + 1):
        ans = min(ans, distances[s][i] + distances[i][a] + distances[i][b])
    return ans


def dijkstra(start, graph, n):
    nodes = [float("inf") for _ in range(n + 1)]
    nodes[start] = 0

    # q = deque()
    # q.append((nodes[start], start))
    q = []
    heapq.heappush(q, (nodes[start], start))

    while q:
        # now_dis, now = q.pop()
        print("현재 노드 : ", q)
        now_dis, now = heapq.heappop(q)
        print("전체 노드 : ", nodes)

        for node, dis in graph[now]:
            sum_dis = now_dis + dis
            if nodes[node] > sum_dis:
                nodes[node] = sum_dis
                # q.append((nodes[node], node))
                heapq.heappush(q, ([nodes[node], node]))

    return nodes


nodes = [6, 7, 6]
starts = [4, 3, 4]
a_nodes = [6, 4, 5]
b_nodes = [2, 1, 6]

fares = [
    [
        [4, 1, 10],
        [3, 5, 24],
        [5, 6, 2],
        [3, 1, 41],
        [5, 1, 24],
        [4, 6, 50],
        [2, 4, 66],
        [2, 3, 22],
        [1, 6, 25],
    ],
    [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
    [
        [2, 6, 6],
        [6, 3, 7],
        [4, 6, 7],
        [6, 5, 11],
        [2, 5, 12],
        [5, 3, 20],
        [2, 4, 8],
        [4, 3, 9],
    ],
]

result = [82, 14, 18]

for n, s, a, b, f in zip(nodes, starts, a_nodes, b_nodes, fares):
    print(solution(n, s, a, b, f))
    print()
