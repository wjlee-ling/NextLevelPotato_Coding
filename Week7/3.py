'''
1번부터 N번까지의 섬
섬 사이의 M개의 다리 (N개 노드, M개 간선, 단방향)
K번째 섬에서 K번째 섬으로 오는 최소한의 거리 (하나 이상의 다른 섬) / 못 돌아오면 -1

idea: 최단 경로를 찾는 bfs
visited를 True, False가 아닌 cn로!!
'''

#import sys
#sys.stdin = open('./quiz/input2.txt', 'r')

from collections import deque

# 1. 입력 받기
n, m, k = map(int, input().split())
'''
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
'''
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
#print(graph)

# 2. BFS
q = deque()
visited = [ 0 for _ in range(n+1)]

# 초기 상태 지정
q.append(k)
visited[k] = 0

while q:
    v = q.popleft()
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            q.append(i)
        if i == k:
            break

if visited[k] == 0:
    print(-1)
else:
    print(visited[k])
