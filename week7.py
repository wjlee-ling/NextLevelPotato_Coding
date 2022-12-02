"""
UXUI 디자이너 (별 1)
"""
'''
1st try: Counter로 계산후 most_common() 사용 -> fail: 11, 18~20
'''

from collections import Counter

N,M = map(int, input().split())

# count
c = Counter()
for _ in range(M):
	events = input().split()[1:]
	c.update(events)
# count가 최댓값과 같은 key들
most = c.most_common(1)[0]
answer  = [k for k, v in c.most_common() if v == most[1]]

# 정렬
answer = reversed(answer)
print(' '.join(list(answer)))

'''
2nd try: fail : 6, 8
'''
from collections import Counter

N,M = map(int, input().split())

# count
c = Counter()
for _ in range(M):
	events = input().split()[1:]
	c.update(events)
"""# count가 최댓값과 같은 key들
most = c.most_common(1)[0]
answer  = [k for k, v in c.most_common() if v == most[1]]

# 정렬
answer = reversed(answer)"""
counts = c.most_common()
counts_sorted = sorted(counts, key=lambda x:(x[1], x[0]), reverse=True)
for k,v in counts_sorted:
	if v == counts_sorted[0][1]:
		print(k, end=' ')

"""
Q2 퍼져나가는 소문
"""

'''
1st_try: 5/6/7 -> fail
union-find algorithm: 부모 노드에 따라 update 되는 알고리즘 시도
'''
from collections import defaultdict
N = int(input()) # 친구 수
M = int(input()) # 관계 수
links = defaultdict(list) 
parents = {i+1: i+1 for i in range(N)} # 처음엔 자기 자신이 부모로 init

def find(node):
	#node(idx)의 root idx를 return
	if parents[node] != node:
		return find(parents[node])
	return node
	
def union(x, y):
	#두 set를 합치고 reset
	x_root = find(x)
	y_root = find(y)
	if x_root < y_root:
		parents[y] = x_root # y node의 root를 x_root로 변경
		# y node의 children node들의 root 도 x_root로 변경
		for link in links[y]:
			if find(link) > x_root:
				parents[link] = x_root
			
	else:
		parents[x] = y_root
		for link in links[x]:
			if find(link) > y_root:
				parents[link] = y_root
	
for _ in range(M):
	u,v = map(int, input().split())
	links[u].append(v)
	links[v].append(u)
	union(u, v)

for parent in parents:
	parents[parent] = find(parent)
	
answer = [k for k, v in parents.items() if v == 1]
print(len(answer))

"""
Q3 구름이의 여행2
"""
'''
1:20 남음
최소 경로: 새 node를 거칠 때 마다 count를 기록하여 마지막에 최소 count를 선택
'''
from collections import defaultdict
N, M, K = map(int, input().split())
links = defaultdict(list)
for _ in range(M):
	a, b = map(int, input().split())
	links[a].append(b) # a -> b 단방향
dist = [N] * (N+1) # min_distance to the idx node
dist[K] = 0
visited = [0] * (N+1)
def update_dist(curr):
	visited[curr] = 1
	for link in links[curr]:
		if dist[link] > dist[curr]+1:
			dist[link] = dist[curr]+1
		if link == K and dist[link] == 0:
			dist[link] = dist[curr]+1
		if visited[link] == 0:
			update_dist(link)
update_dist(K)

if dist[K]==0:
	print(-1)
else:
	print(dist[K])

"""
Q4. 이상한 미로 Dijkstra!!!!
"""

from collections import defaultdict
"""
dfs로 cost1, cost2 를 노드 이동시마다 업데이트 하기
"""

N, M = map(int, input().split())
als = list(map(int, input().split()))
links = defaultdict(list)
times = [[0]*N for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    links[u].append(v)
    links[v].append(u)
    times[u][v] = w
    times[v][u] = w
visited = [0] * (N+1)
def route(curr, visited, time, cost):
    '''time: curr올 때까지 누적 시간, cost: 나머지'''
    visited = visited.copy()
    visited[curr] = 1
    for _next in links[curr]:
        if visited[_next] == 1:
            continue
        new_cost = _next % 