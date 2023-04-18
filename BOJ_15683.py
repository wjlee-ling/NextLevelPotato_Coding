import sys; readl = sys.stdin.readline

r, c = map(int, readl().split())
graph, cams, n_walls = [], [], 0
for i in range(r):
    row = readl().strip().split()
    graph.append(row)
    for j in range(c):
        if 1 <= int(row[j]) <= 5:
            cams.append((i,j))
        elif int(row[j]) == 6:
            n_walls += 1

n_cams = len(cams)
moves = [(-1,0), (0,1), (1,0), (0,-1)] # N, E, S, W
max_seen = 0

def is_valid(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    if graph[x][y] == "6":
        return False

    return True

def watch(x,y,heading):
    # mark "#"
    dx,dy = moves[heading]
    watchable = set()
    while is_valid(x+dx,y+dy):
        watchable.add((x+dx, y+dy))
        x,y = x+dx, y+dy
    return watchable

def watch_all_directions(x,y):
    results = []
    for heading in range(4):
        results.append(watch(x,y,heading))
    return results

def get_headings(type):
    if type == "1":
        return [(0,),(1,),(2,),(3,)]
    elif type == "2":
        return [
            (0,2), (1,3)
        ]
    elif type == "3":
        return [
            (0,1),(1,2),(2,3),(3,0)
        ]
    elif type == "4":
        return [
            (3,0,1),(0,1,2),(1,2,3),(2,3,0)
        ]
    else:
        return [(0,1,2,3)]

def search(seen_sofar):
    
    if cams:
        cx, cy = cams.pop()
        watches = watch_all_directions(cx,cy) # 4방향 감시 가능 지ㄱ
        for combns in get_headings(graph[cx][cy]):
            # 카메라별 패턴 # e.g. (0,2) or (1,3) for 2nd camera type
            seen_per_combn = set()
            for heading in combns:
                seen_per_combn = seen_per_combn.union(watches[heading])
            search(seen_sofar | seen_per_combn)

    else:
        black = 0
        global ans
        for i in range(r):
            for j in range(c):
                if (i,j) not in seen_sofar:
                    black += 1
        ans = min(ans, black)
        if ans == black:
            print(sorted(seen_sofar, key=lambda x: (x[0],x[1])))
        return ans

ans = float("inf")
search(set())
# print(max_seen, n_cams, n_walls)
# ans = r*c - max_seen - n_cams - n_walls
print(ans)