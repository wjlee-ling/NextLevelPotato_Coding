from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    dict = {}
    for u, v in roads:
        if u not in dict.keys():
            dict[u] = [v]
        else:
            dict[u].append(v)
        if v not in dict.keys():
            dict[v] = [u]
        else:
            dict[v].append(u)
    
    

    queue = deque([destination])
    visited = [-1] * (n+1)
    visited[destination] = 0

    while queue:
        now = queue.popleft()
        if now in dict.keys():
            for w in dict[now]:
                if visited[w] == -1:
                    queue.append(w)
                    visited[w] = visited[now]+1
                        
    
    return [visited[i] for i in sources]
    
