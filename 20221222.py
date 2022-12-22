# 출발지점 S에서 K까지 합승하고 각각 A, B로 가는 최단경로를 구하는 문제
# S~K 까지의 최단거리 + K~A 까지의 최단거리 + K~B 까지의 최단거리

# 다익스트라
import heapq

def solution(n, s, a, b, fares):
    """
    Args:
        n (int) : 지점의 총 개수
        s (int) : 출발 지점
        a (int) : A의 목적지
        b (int) : B의 목적지
        fares (2d list[int]) : 지점 사이의 택시요금 배열이 담긴 배열 
    """
    graph = [[] for _ in range(n+1)]

    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    def dijkstra(start):
        dist_check = [float("inf")] * (n+1)
        dist_check[start] = 0
        q = []
        heapq.heappush(q, (start, 0))

        while q:
            node, dist = heapq.heappop(q)
            for next_node, next_dist in graph[node]:
                if dist + next_dist < dist_check[next_node]:
                    dist_check[next_node] = dist + next_dist
                    heapq.heappush(q, (next_node, dist_check[next_node]))
        return dist_check
    

    answer = float("inf")
    dist = [[]]
    for i in range(1, n+1):
        dist.append(dijkstra(i))

    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer


# 플로이드 와샬
# 다익스트라 알고리즘은 한 지점에서 다른 모든 지점까지의 최단 경로를 계산하는 알고리즘이다. 
# 플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 계산하는 알고리즘

## 플로이드는 i에서 출발해 j로 가는 경로의 가중치를 저장하는 2차원 배열을 채우는데, 
## i를 출발해 j로 바로 가는 것보다 k를 거쳐 j로 가는 게 효율적일 경우(저렴할 경우) 해당 값을 갱신함

def solution(n, s, a, b, fares):
    """
    Args:
        n (int) : 지점의 총 개수
        s (int) : 출발 지점
        a (int) : A의 목적지
        b (int) : B의 목적지
        fares (2d list[int]) : 지점 사이의 택시요금 배열이 담긴 배열 
    """
    graph = [[float("inf")] * (n+1) for _ in range(n+1)]

    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    for i in range(1, n+1):
        graph[i][i] = 0
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    return min(graph[s][i] + graph[i][a] + graph[i][b] for i in range(1, n+1))