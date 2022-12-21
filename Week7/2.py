ing korean
N = int(input())
M = int(input())

dict = {}
for _ in range(M):
        u, v = map(int, input().split())
            if u not in dict.keys():
                        dict[u] = [v]
                            else:
                                        dict[u].append(v)
                                                
                                                    if v not in dict.keys():
                                                                dict[v] = [u]
                                                                    else:
                                                                                dict[v].append(u)
                                                                                        

                                                                                        queue = [1]
                                                                                        visited = []
                                                                                        answer = 0
                                                                                        if 1 not in dict.keys():
                                                                                                print(1)
                                                                                                    quit()

                                                                                                    while queue:
                                                                                                            now = queue.pop(0)
                                                                                                                if now in dict.keys():
                                                                                                                            for w in dict[now]:
                                                                                                                                            if w not in visited:
                                                                                                                                                                visited.append(w)
                                                                                                                                                                                queue.append(w)
                                                                                                                                                                                                answer += 1

                                                                                                                                                                                                print(answer)
