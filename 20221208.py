"""
solved
"""


from collections import deque


def solution(n, roads, sources, destination):
    answer = [-1] * (n + 1)

    graph = [[] * (n + 1) for _ in range(n + 1)]
    for r1, r2 in roads:
        graph[r1].append(r2)
        graph[r2].append(r1)

    q = deque()
    q.append([destination, 0])
    visited = [0] * (n + 1)

    while q:
        now, dis = q.popleft()
        if now == destination:
            visited[now] = 1
            answer[now] = 0

        for g in graph[now]:
            if visited[g] == 0:
                # print(now, g, dis, answer)
                visited[g] = 1
                q.append([g, dis + 1])
                if g in sources:
                    answer[g] = dis + 1

    # for i, source in enumerate(sources):
    #     q = deque()
    #     q.append([source, 1])
    #     visited = [0] * (n + 1)

    #     while q:
    #         s, dis = q.popleft()
    #         if s == destination:
    #             answer[i] = 0
    #             break

    #         if visited[s] == 0:
    #             visited[s] = 1
    #             for g in graph[s]:
    #                 q.append([g, dis + 1])
    #                 if g == destination:
    #                     answer[i] = dis
    #                     q.clear()

    return [answer[i] for i in sources]


if __name__ == "__main__":
    nums = [3, 5]
    roads = [[[1, 2], [2, 3]], [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]]
    sources = [[2, 3], [1, 3, 5]]
    destination = [1, 5]
    results = [[1, 2], [2, -1, 0]]
    for n, road, source, dest in zip(nums, roads, sources, destination):
        print(solution(n, road, source, dest))
