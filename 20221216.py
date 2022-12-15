"""
solved
"""

from collections import defaultdict
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    answer = [0, float("inf")]
    summits = sorted(summits)
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    hq = []
    visited = [float("inf")] * (n + 1)

    for gate in gates:
        heappush(hq, [0, gate])
        visited[gate] = 0

    while hq:
        intensity, node = heappop(hq)
        if node in set(summits) or intensity > visited[node]:
            continue

        for n, w in graph[node]:
            new_intensity = max(intensity, w)
            if new_intensity < visited[n]:
                visited[n] = new_intensity
                heappush(hq, [new_intensity, n])

    for summit in summits:
        if visited[summit] < answer[1]:
            answer[0] = summit
            answer[1] = visited[summit]

    return answer


if __name__ == "__main__":
    nums = [6, 7, 7, 5]
    paths = [
        [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
        [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
        [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
        [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],
    ]
    gates = [
        [1, 3],
        [1],
        [3, 7],
        [1, 2],
    ]
    summits = [
        [5],
        [2, 3, 4],
        [1, 5],
        [5],
    ]
    result = [
        [5, 3],
        [3, 4],
        [5, 1],
        [5, 6],
    ]

    for n, path, gate, summit in zip(nums, paths, gates, summits):
        print(solution(n, path, gate, summit))
