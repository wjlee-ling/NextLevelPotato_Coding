# Testcase 2/4/6/7/10/11/12/13/14/16 → FAIL

# 나라 개수 : N
# 다리 개수 : M
# 구름이의 현재 위치 섬 : K

# 단방향

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	
global count, flag
count = 0
flag = False
	

def dfs(v):
	global count, flag
	visited[v] = True
	for i in graph[v]:
		if i == K:
			flag = True
			break
		if not visited[i]:
			count += 1
			dfs(i)

dfs(K)

if flag:
	print(count)
else:
	print(-1)


########################################################
# 최소 길이의 사이클을 찾아야하므로 DFS보다 BFS가 더 적합하다.

# DFS
## 모든 정점 탐색에 O(N+M)
## 장점 : 한번에 한 정점(및 지나온 경로 정점)만 확인, 모든 경우를 구해야할 때 유용함
## 단점 : 주로 재귀로 구현되므로, 스택 메모리 제한 우려

# BFS
## 모든 정점 탐색에 O(N+M)
## 장점 : 멀지 않은 거리에 구하고자 하는 정점이 있는 경우 DFS보다 현저히 빠름
## 단점 : 큐에 많은 정점을 저장(O(N) 공간)

import sys
from collections import defaultdict
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
graph = defaultdict(list) # 단방향 그래프
for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b) # # defaultdict(<class 'list'>, {1: [2, 4], 3: [1], 4: [2, 5], 5: [3]})

q = deque() # 탐색 순서 관리
q.append(K) # 시작 섬 입력
visited = [0 for _ in range(N+1)]

while q:
	target = q.popleft()

	for next_target in graph[target]:
		if visited[next_target] == 0:
			visited[next_target] = visited[target] + 1 # next_target 섬까지 거친 섬 수를 visited에 저장
			q.append(next_target)
		
		if next_target == K:
			break

if visited[K] == 0:
	print(-1)
else:
	print(visited[K])
