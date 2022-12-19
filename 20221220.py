# 1번 마을에서 다른 마을로 가는 최단경로, edge가 있으므로 다익스트라

import heapq

def dikstra(graph, dist_check):
    q = []
    heapq.heappush(q, (1, 0)) # node, dist

    while q:
        node, dist = heapq.heappop(q)
        for next_node, next_dist in graph[node]:
            if dist + next_dist < dist_check[next_node]:
                dist_check[next_node] = dist + next_dist
                heapq.heappush(q, (next_node, dist_check[next_node]))



def solution(N, road, K):
    """
    Args:
        N (int) : 마을의 개수
        road : 각 마을을 연결하는 도로의 정보가 담긴 2차원 배열
        K (int) : 음식 배달이 가능한 시간
        
    Returns:
        K시간 이하로 배달이 가능한 음식 주문을 받을 수 있는 마을의 개수
    """
    graph = [[] for _ in range(N+1)] 
    dist_check = [float("inf")] * (N+1)  # 최단경로 저장
    dist_check[1] = 0  # 1번 마을에서 1번 마을로 가는 거리는 0

    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    dikstra(graph, dist_check)

    return len([i for i in dist_check if i <= K])