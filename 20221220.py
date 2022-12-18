'''
N개의 마을 중 K 시간 이하로 배달이 가능한 마을에서만 주문을 받는다
1번 노드에서 음식 주문을 받을 수 있는 마을의 개수 return
'''
from collections import defaultdict
from heapq import heappop, heappush

def solution(N, road, K):
    graph = defaultdict(list)
    for r in road:
        node1, node2, cost = r[0], r[1], r[2]
        graph[node1].append((cost, node2)) # graph랑 distance 둘 다 cost, node 순서로 삽입
        graph[node2].append((cost, node1))
    INF = float('inf')
    distance = [INF]*(N+1)
    
    def dijkstra(start):
        q = []
        heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, node = heappop(q)
            if distance[node] < dist:
                continue
            for next_cost, next_node  in graph[node]:
                cost = distance[node] + next_cost
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heappush(q, (cost, next_node))
    dijkstra(1)
    answer = 0
    for d in distance:
        if d <= K:
            answer +=1 
    return answer