from collections import defaultdict
import heapq as hq

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for fare in fares:
        node1, node2, cost = fare[0], fare[1], fare[2]
        graph[node1].append([cost, node2])
        graph[node2].append([cost, node1])
    INF = float('INF')
    
    def dijkstra(start, end):
        distance = [INF]*(n+1)
        queue = []
        hq.heappush(queue, [0, start])
        distance[start] = 0
        
        while queue:
            dist, node = hq.heappop(queue)
            if distance[node] < dist:
                continue
            for next_cost, next_node in graph[node]:
                cost = next_cost + distance[node] 
                if cost < distance[next_node]: 
                    distance[next_node] = cost
                    hq.heappush(queue, [cost, next_node])
        return distance[end]

    
    answer = INF
    for i in range(1, n+1):
        if i != s:
            answer = min(answer, (dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b)) )
    answer = min(answer, dijkstra(a, s) + dijkstra(b, s))
    return answer