n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(line, i, j, pos):
    # line : row(pos=0) or col(pos=1)
    new_seen = set()
    for idx in range(1, len(line)):
        # same level
        if idx > 0 and line[idx-1] == line[idx]:
            continue
        # diff
        else:
            check = 0
            while check < l :          
                if line[idx] > line[idx-1]:
                    # 왼쪽으로 다리
                    next_idx = idx-1-check
                else:
                    # 오른쪽으로 다리
                    next_idx = idx+check

                # diff is more than 1
                if next_idx < 0 or next_idx > 0 or abs(line[idx] - line[next_idx]) != 1:
                    return False
                # mark bridges
                if pos == 0:
                    if (i,next_idx) in new_seen: # se
                        return False
                    new_seen.add((i,next_idx))
                else:
                    if (next_idx, j) in new_seen:
                        return False
                    new_seen.add((next_idx, j))
                check += 1
                
    new_seen.add((-1,-1)) # add dummy seen node for row/col with the same level
    return new_seen

cnt = 0
# row-wise
pos = 0
for i in range(len(graph)):
    new_seen = dfs(graph[i], i, 0, 0)
    if new_seen:
        print(i, new_seen)
        cnt +=1 
print("==============")
pos = 1
seen = set()
graph = list(zip(*graph))
for i in range(len(graph)):
    new_seen = dfs(graph[i], 0, i, 1)
    if new_seen:
        cnt += 1
        print(i, new_seen)
print(cnt)