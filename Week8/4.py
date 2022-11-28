'''
N개의 도시. N-1개의 도로 (양방향)
i번 도시에 쓰레기 Ai 
K만큼 담을 수 있는 쓰레기 봉투 / 방문하지 않은 인접 노드에서 봉투가 찰 때까지 (**노드를 방문해도 쓰레기 안 치울 수 있음**)

return: 구름이가 모을 수 있는 최대 쓰레기 양
idea: 가중치가 있는 노드 -> 다익스트라 / 노드까지의 거리가 가중치가 아니라 도착해서 치울 지 말지
'''
import sys
input = sys.stdin.readline

# 1. 입력 받기
N, K = map(int, input().split())
node = [[] for _ in range(N+1)] # 인접 리스트
for _ in range(N-1):
	a, b= map(int, input().split())
	node[a].append(b)
	node[b].append(b)
trashes = list(map(int, input().split()))


visited = [False for _ in range(N)]

	





