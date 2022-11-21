# 친구 수 : N
# 친구 관계의 수 : M

# 1번 비밀을 아는 사람 수를 구하기

import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
global answer
answer = 1


def dfs(v):
	global answer
	visited[v] = True
	for i in graph[v]:
		if not visited[i]:
			answer += 1
			dfs(i)

dfs(1)
print(answer)