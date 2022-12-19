'''
n: 지점의 개수
s: 출발 지점
A: a의 도착 지점
B: b의 도착 지점
fares: 지점 사이의 요금

s에서 출발해서 각각의 도착 지점까지 택시를 타고 갈 때의 최저 예상 택시 요금
(각자 이동도 가능)

s에서 a,b가 아닌 지점까지 가는 값 저장 + 공동지점에서 a,b까지 (다익스트라 사용)
'''
from collections import defaultdict
from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for fare in fares:
        node1, node2, cost = fare[0], fare[1], fare[2]
        graph[node1].append((cost, node2))
        graph[node2].append((cost, node1))
    
    def dijkstra(start, end): # start에서 출발해서 end까지의 최소 cost
        INF = float('inf')
        distance = [INF]*(n+1)
        q = []
        heappush(q, (0, start))
        distance[start] = 0 #
        
        while q:
            dist, node = heappop(q)
            if distance[node] < dist: # distance를 갱신하려고 하는데 이미 더 작음
                continue
            for next_cost, next_node in graph[node]: # graph를 통해 다음에 방문할 노드 찾기
                cost = next_cost + distance[node] 
                if cost < distance[next_node]: 
                    distance[next_node] = cost
                    heappush(q, (cost, next_node))
        return distance[end]
    

    # 1. 합승 안하는 경우
    not_together = dijkstra(s, a)+ dijkstra(s, b)
    
    # 2. 합승하는 경우
    answer = float('inf')
    for i in range(1, n+1):
        if i != s:
            answer = min(answer, (dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b)) )
        
    return min(not_together, answer)