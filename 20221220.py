from collections import defaultdict, deque


def solution(N, road, K):
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    q = deque()
    q.append([1, 0])
    dist = [float("inf")] * (N + 1)
    dist[1] = 1

    while q:
        node, weight = q.popleft()
        for n, w in graph[node]:
            if weight + w <= dist[n]:
                dist[n] = weight + w
                q.append([n, weight + w])
        # print(dist)

    answer = len([i for i in dist if i <= K])

    return answer


if __name__ == "__main__":
    N = [5, 6]
    roads = [
        [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]],
        [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]],
    ]
    K = [3, 4]
    result = [4, 4]
    for n, road, k in zip(N, roads, K):
        print(solution(n, road, k))
