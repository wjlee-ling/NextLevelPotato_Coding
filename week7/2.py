'''
N 명의 친구(1~N번)와 M 쌍의 친구 관계 (양방향 친구)
1번 친구한테 소문을 퍼뜨렸을 때 소문을 듣게 될 친구가 몇 명?

처음 접근법은 "서로소 집합을 활용한 사이클 판별"이었음 (틀림)
하지만 1번노드에서 각 노드까지 연결이 가능하냐가 핵심이지, 사이클을 찾는 문제가 아님!
모든 경우를 구해야 하므로 DFS
'''
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)] # 인접 리스트
node = [0 for _ in range(N + 1)] # 각 노드가 1과 연결되어있으면 1, 아니라면 0(인덱스 값이 노드 번호)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph) #[[], [3], [3, 4], [1, 2, 4], [3, 5, 2], [4]]

def DFS(n):
    for next in graph[n]:
        if node[next]: # 이미 방문했다면 pass
            continue
        node[next] = 1
        DFS(next)
        
node[1] = 1
DFS(1)
#print(node) # [0, 1, 1, 1, 1, 1]
print(sum(node))
