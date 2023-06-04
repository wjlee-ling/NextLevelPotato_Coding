import sys

sys.setrecursionlimit(10000)

xmoves = [-1, 0, 1, 0]  # 상 우 하 좌
ymoves = [0, 1, 0, -1]

N = int(input())
graph = [[0] * N for _ in range(N)]
apples = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    apples[x - 1][y - 1] = 1

L = int(input())
directions = {}
for _ in range(L):
    x, c = input().split()
    directions[int(x)] = c


def is_valid(nx, ny):
    # if 0 > nx or nx >= N or 0 > ny or ny >= N:
    #     return False
    # if graph[nx][ny] == 1:
    #     return False
    return 0 <= nx < N and 0 <= ny < N


def change_dir(ts, dir):
    """ts : timestep"""
    if ts in directions:
        d = directions[ts]
        if d == "L":
            # 반시계
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
    return dir


def move(x, y, ts, dir, length):
    # print(ts)
    nx = x + xmoves[dir]
    ny = y + ymoves[dir]
    if not is_valid(nx, ny):
        # 벽
        return ts
    elif (
        is_valid(nx, ny) and graph[nx][ny] > 0 and ts - length <= graph[nx][ny]
    ):  # ts: 5 // len: 3 = [2,3,4] //
        # 뱀
        return ts

    if apples[nx][ny] == 1:
        apples[nx][ny] = 0
        length += 1
    graph[nx][ny] = ts
    dir = change_dir(ts, dir)
    ans = move(nx, ny, ts + 1, dir, length)
    return ans


ts = 1
dir = 1  # 오른쪽
length = 1

ans = move(0, 0, ts, dir, length)
print(ans)
