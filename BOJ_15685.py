dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
graph = [[0]*101 for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1
    past = [d]
    for _ in range(g):
        new = []
        for i in range(len(past)):
            new.append((past[-i-1] + 1) % 4)
        past.extend(new)

    for i in past:
        nx = x + dx[i]
        ny = y + dy[i]
        graph[nx][ny] = 1
        x, y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]:
            if graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
                # 정사각형
                ans += 1
print(ans)