# 양방향 통행 가능
# 출입구 출발해서 산봉우리 중 한 곳만 방문한 뒤 원래의 출입구로 돌아오기

# intensity : 휴식 없이 이동해야 하는 시간 중 가장 긴 시간
## edge들의 누적값이 아닌 경로들의 intensity 중 최솟값을 찾아야 함
## 매 edge의 가중치가 다르고, 최솟값을 찾아야 하므로 다익스트라를 떠올려야 함

# 산봉우리를 찍고 내려오는 길의 intensity까지 찾지 않아도 됨
## 경로에서 우리가 찾고자 하는 것은 edge의 최댓값



# https://hz25.tistory.com/6

from collections import defaultdict
from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    """
    Args: 
        n (int) : 산의 지점 수
        paths : 각 등산로의 정보를 담은 2차원 정수 배열 [i,j,w] = i번 지점과 j번 지점을 연결, w는 두 지점 사이 이동 시간
        gates : 출입구 번호 배열
        summits : 산봉우리들의 번호가 담긴 정수 배열
    Returns:
        [산봉우리 번호, intensity 최솟값]
    """

    def get_min_intensity():
        i_node_list = [] # (intensity, 현재 위치)
        visited = [10000001]*(n+1)

        # 모든 출발지를 우선순위 큐에 삽입
        for gate in gates:
            heappush(i_node_list, (0, gate))
            visited[gate] = 0
        
        # 산봉우리에 도착하거나 더 큰 intensity면 멈춤
        while i_node_list:
            intensity, node = heappop(i_node_list)
            if node in summits or intensity > visited[node]:
                continue
            
            # 인접한 노드로 이동
            for weight, next_node in graph[node]:
                new_intensity = max(intensity, weight)

                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heappush(i_node_list, (new_intensity, next_node))

        min_intensity = [0, 10000001]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity = [summit, visited[summit]]
        return min_intensity
            
    summits.sort()

    # 1. 그래프 생성
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    return get_min_intensity()



# --------------------------------------

def solution(n, paths, gates, summits):
    graph = {}
    answer = [-1, 10000001]

    for i, j, w in paths:
        for x, y in ((i, j), (j, i)):
            if x not in graph:
                graph[x] = [(y, w)]
            else:
                graph[x].append((y, w))

    intensity = [10000001] * (n + 1)

    for gate in gates:
        intensity[gate] = 0

    check = set(summits)
    stack = gates

    while stack:
        target = set()

        while stack:
            curr_node = stack.pop()

            for next_node, weight in graph[curr_node]:
                max_weight = max(intensity[curr_node], weight)

                if intensity[next_node] > max_weight:
                    intensity[next_node] = max_weight

                    if next_node not in check:
                        target.add(next_node)

        stack = list(target)

    return min(
        ([summit, intensity[summit]] for summit in summits),
        key=lambda x: (x[1], x[0]),
    )