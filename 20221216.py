'''
n개의 지점으로 이루어진 산
intensity: 휴식 없이 이동해야 하는 가장 긴 시간

출구에서 입구까지 산봉우리를 한 번씩 가면서 intensity가 최소가 되도록
출입구인 노드는 처음과 끝에서만 나올 수 있음

------------------------------------------
n: 산의 지점 수
paths: 각 등산로의 정보를 담은 2차원 arr   [a,b,c] : a와 b가 이어져 있고 걸리는 시간은 c
gates: 출입구의 번호가 담긴 arr
summits: 산봉우리의 번호가 담긴 arr    gates와 summit이 아니면 쉼터인 노드

intensity가 최소가 되는 코스의 (산봉우리, 그때의 intensity 값)
여러 개라면 산봉우리가 적은 경우로 return
------------------------------------------
dijkstra
'''
from heapq import heappop, heappush
from collections import defaultdict

def solution(n, paths, gates, summits): # gate -> summits -> 같은 gate

    def dijkstra(): # ⭐start로 gates 원소들 별도로 받을 필요 없음
        q = [] #(intensity, node 번호)
        INF = int(1e9)
        distance = [INF]*(n+1) # 노드 별 최단 거리 기록
        
        # 모든 출발지(gates)를 큐에 삽입
        for gate in gates: 
            heappush(q, (0, gate))
            distance[gate] = 0
        
        while q:
            intensity, node = heappop(q) # intensity가 가장 짧은 노드에 대한 정보를 꺼낸다
            
            if (node in summits_set) or (distance[node] < intensity): 
                # 봉우리에 도착했거나 현재 노드가 이미 처리된 적 있다면 무시 
                continue
                
            for weight, next_node in graph[node]: # 현재 노드에 연결된 노드 확인
                new_intensity = max(intensity, weight) # dist가 아닌 intensity로 갱신⭐
                if new_intensity < distance[next_node]: # 갱신
                    distance[next_node] = new_intensity
                    heappush(q, (new_intensity, next_node))
                    
        # [산봉우리 번호, intensity 값] 반환
        answer = [0, INF]
        for summit in summits:
            if distance[summit] < answer[1]:
                answer[0] = summit
                answer[1] = distance[summit]
            
        return answer
    #------------------------------------------
    summits.sort()
    summits_set = set(summits) # ⭐
    
    graph = defaultdict(list) # ⭐ 노드 간 연결 기록    
    for path in paths:
        node1, node2, cost = path[0], path[1], path[2]
        graph[node1].append((cost, node2)) # (cost, node)
        graph[node2].append((cost, node1))
         
    return dijkstra()

# https://hz25.tistory.com/6