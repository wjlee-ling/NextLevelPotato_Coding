### 일부 테케 오답 ###
'''
N개의 방(번호가 1~N), M개의 복도로 이루어진 미로(양방향) / 복도 마다 이동시간이 있음
i번방 ~ j번방 / j번방 ~ k번방 
=> i에서 k번방으로 이동할 때 i % Aj == k % Aj
각 방의 바닥에는 1~10까지 정수 Ai가 쓰여짐

1번방에서 N번방까지 미로 탈출이 가능한가? 얼마나 걸리는가?
idea: 다익스트라
'''

import heapq
#import sys
#sys.stdin = open('./quiz/input.txt', 'r')

# 1. 입력 받기
N, M = map(int, input().split()) # 방, 복도의 개수
A = [0] + list(map(int, input().split())) # 각 방 바닥에 적혀 있는 수 (idx 0 추가하기!!)
graph = [[] for _ in range(N+1)] # 인접 리스트

for _ in range(M):
    a,b,c = map(int, input().split()) #a번방과 b번방이 연결되어 있고 걸리는 시간은 c
    graph[a].append([b,c])
    graph[b].append([a,c])
#print(graph)

INF = int(1e9)
distance = [[INF for _ in range(10)] for _ in range(N + 1)] 
# distance = [INF] * (N+1)

answer = -1
# 2. 다익스트라 실행

# 초기 상태
q = []
distance[1][0] = 0 # 시작노드->시작노드 거리 기록
heapq.heappush(q, (distance[1][0], 1, 0))  
# heap에 (거리, 다음 노드, 현재에서 다음노드로 갈 때 Aj나눈 값) 저장
# 시작노드로 가기 위한 최단 경로는 0으로 설정

while q:
    dist, cur, prev = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    if dist > distance[cur][prev]: # 현재 노드가 이미 처리된 적 있다면 무시
        continue
    if cur == N:
        answer = dist
        break
    for next, nd in graph[cur]: # 현재 노드와 연결된 노드 확인
        # graph[node1] = (node2, cost) / next = [node2, cost]
        if dist + nd >= distance[next][cur % A[next]]: 
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 긴 경우
            continue
        if cur != 1 and prev % A[cur] != next % A[cur]:
            # Aj로 나눈 거 체크
            continue
        # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧고 Aj로 나눈 거 동일
        distance[next][cur % A[next]] = dist + nd
        heapq.heappush(q, (dist+nd, next, cur % A[next]))

print(answer)
