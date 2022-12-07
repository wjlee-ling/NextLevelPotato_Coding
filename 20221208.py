def solution(n, roads, sources, destination):
    from collections import deque
    
    # try 1: dictionary => failure: 6~ 15
    # shortest => bfs starting from destination
    answer = []
    
    # creating map
    links = dict()
    for a,b in roads:
        links[a] = links.get(a, []) + [b]
        links[b] = links.get(b, []) + [a]
        
    queue = deque([destination])
    visited = [0] * (n+1)
    inf = 100000
    shortest = [inf] * (n+1)
    dist = 0
    while queue:
        curr = queue.popleft()
        visited[curr] = 1
        
        dist += 1
        if links.get(curr, None):
            for node in links[curr]:
                if visited[node] == 0:
                    queue.append(node)
                shortest[node] = min(shortest[node], dist)
    for s in sources:
        if s == destination:
            answer.append(0)
        elif shortest[s] == inf:
            answer.append(-1)
        else:
            answer.append(shortest[s])
    return answer
