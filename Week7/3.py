'''
1번부터 N번까지의 섬
섬 사이의 M개의 다리 (N개 노드, M개 간선, 단방향)
K번째 섬에서 K번째 섬으로 오는 최소한의 거리 (하나 이상의 다른 섬) / 못 돌아오면 -1

idea: 최단 경로를 찾는 bfs
*** 시간 초과
'''

from collections import deque
import sys
sys.stdin = open('./quiz/input2.txt', 'r')

def BFS(v, cnt):
    queue = deque([v]) # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    visited[v] = True
    while queue: # 큐가 빌 때까지
        v = queue.popleft() # 큐에서 하나의 원소를 뽑아 출력
        print(v)

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                cnt +=1 
                queue.append(i)
                visited[i] = True

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
print(graph)

visited = [False]*(M+1)
cnt = 0
BFS(1, cnt)


