"""
퍼져나가는 소문 (별 2)
"""
7
5
1 4
3 5
7 6
1 5
4 3

4

5
5
1 3
2 3
3 4
4 5
4 2

5

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
