ing korean
N, M, K = map(int, input().split())
dict = {}
for _ in range(M):
        u, v = map(int, input().split())
            if u not in dict.keys():
                        dict[u] = [v]
                            else:
                                        dict[u].append(v)
                                            
                                            #print(dict)
                                                    
                                                    queue = [K]
                                                    visited = [0] * (N+1)

                                                    while queue:
                                                            now = queue.pop(0)
                                                                if now in dict.keys():
                                                                            for w in dict[now]:
                                                                                                if visited[w] == 0:
                                                                                                                            visited[w] = visited[now] + 1
                                                                                                                                                    queue.append(w)
                                                                                                                                                                    if w == K:
                                                                                                                                                                                                break

                                                                                                                                                                                            if visited[K] == 0:
                                                                                                                                                                                                    print(-1)
                                                                                                                                                                                                else:
                                                                                                                                                                                                        print(visited[K])

