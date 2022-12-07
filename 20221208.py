'''
[input]
n: 지역 수
roades: 두 지역을 왕복할 수 있는 길의 정보 
sources: 각 부대원이 위치한 서로 다른 지역을 나타내는 정수
destination: 강철부대의 지역

[output]
sources의 원소 순서대로 강철부대로 복귀할 수 있는 최단시간을 담은 배열

[idea]
BFS - deque, 인접 리스트, visited
'''
from collections import deque    
        
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)] # 인접 리스트
    for road in roads:
        a, b = road[0], road[1]
        graph[a].append(b)
        graph[b].append(a)
    # print(nodes)
    
    ans = [-1 for _ in range(n+1)]
    ans[destination] = 0
    Q = deque([destination])
    visited = set([destination]) # 원소 중복 없이 add하려고 집합 사용
    while Q:
        node = Q.popleft()
        for x in graph[node]:
            if x not in visited:
                visited.add(x)
                ans[x] = ans[node]+1
                Q.append(x)
                
    return list(ans[s] for s in sources)



''' 오답 
from collections import deque
def bfs(n, visited, nodes, start, end):
    q = deque()
    q.append(start)
    visited[start] = 1
    num = 0
    while q:
        tmp = q.popleft()
        num += 1
        if tmp == end:
            return num
        for i in nodes[tmp]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1       
        
def solution(n, roads, sources, destination):
    answer = []
    nodes = [[] for _ in range(n+1)] # 인접 리스트
    for road in roads:
        a, b = road[0], road[1]
        nodes[a].append(b)
        nodes[b].append(a)
    # print(nodes)
    
    visited = [0]*(n+1)
    for source in sources:
        answer.append(bfs(n, visited, nodes, source, destination))
    return answer
'''