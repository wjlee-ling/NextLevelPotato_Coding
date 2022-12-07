# sources의 각 원소마다 destination으로 복귀할 수 있는 최단 시간을 반환해야 함
# 최단 시간(거리)이므로 BFS를 사용
# destination 지점에서 sources로 각각 도착하는 거리를 계산

from collections import deque

def solution(n, roads, sources, destination):
    """
    Args:
        n (int) : 총 지역의 수
        roads : 두 지역을 왕복할 수 있는 길 정보를 담은 2차원 정수 배열
        sources : 각 부대원이 위치한 서로 다른 지역들을 나타내는 정수배열
        destination : 강철부대의 지역
    Returns:
        주어진 sources의 원소 순서대로 강철부대로 복귀할 수 있는 최단 시간
    """
    visited = [-1 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for v1, v2 in roads:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    queue = deque([destination])
    visited[destination] = 0

    while queue:
        curr_node = queue.popleft()

        for node in graph[curr_node]:
            if visited[node] == -1:
                visited[node] = visited[curr_node] + 1
                queue.append(node)
    
    return [visited[i] for i in sources]