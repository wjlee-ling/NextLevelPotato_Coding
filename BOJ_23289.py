"""
23289. 온풍기 안녕!
"""


from collections import deque


def solution():
    R, C, K = map(int, input().split())
    heater = []  # 온풍기 위치 (y, x, dir)
    check_pos = []  # 확인할 온도 위치 (y, x)
    for i in range(R):
        temp = list(map(int, input().split()))
        for j, k in enumerate(temp):
            if 1 <= k <= 4:
                heater.append([i, j, k])
            elif k == 5:
                check_pos.append([i, j])

    wall_board = [[[0] * 5 for _ in range(C)] for _ in range(R)]  # [y][x][-, 우, 좌, 상, 하]

    W = int(input())
    for _ in range(W):
        y, x, t = map(int, input().split())
        y -= 1
        x -= 1

        if t == 0:  # t가 0이면 상하를 막는 벽
            wall_board[y][x][3] = 1  # 상
            if y == 0:
                continue
            wall_board[y - 1][x][4] = 1  # 하

        if t == 1:  # t가 1이면 좌우를 막는 벽
            wall_board[y][x][1] = 1  # 우
            if x == C - 1:
                continue
            wall_board[y][x + 1][2] = 1  # 좌

    board = [[0] * C for _ in range(R)]

    # 우좌상하 (바람이 퍼져갈 때 3칸씩 퍼져나감)
    dy = [[], [-1, 0, 1], [-1, 0, 1], [-1, -1, -1], [1, 1, 1]]
    dx = [[], [1, 1, 1], [-1, -1, -1], [-1, 0, 1], [-1, 0, 1]]

    def isin(y, x):
        if 0 <= y < R and 0 <= x < C:
            return True
        return False

    def isnext(y, x, t, idx):
        if idx == 1:  # 일직선 방향 체크
            if wall_board[y][x][t]:
                return False
            else:
                return True

        # (y,x)에서 (y-1,x+1)로 바람이 이동하려면(= 바람이 대각선 위쪽으로 이동하려면) (y,x)와 (y-1,x) 사이, (y-1,x)와 (y-1,x+1) 사이에 모두 벽이 없어야 한다.
        # (y,x)에서 (y+1,x+1)로 바람이 이동하려면(= 바람이 대각선 아래쪽으로 이동하려면) (y,x)와 (y+1,x) 사이, (y+1,x)와 (y+1,x+1) 사이에 모두 벽이 없어야 한다.
        if t == 1:
            ny = y + dy[t][idx]
            if 0 <= ny < R:
                temp_walls = wall_board[ny][x]
                if idx == 0:  # 대각선 위
                    if temp_walls[1] or temp_walls[4]:  # 벽이 오른쪽, 아래쪽
                        return False
                    return True
                elif idx == 2:  # 대각선 아래
                    if temp_walls[1] or temp_walls[3]:  # 벽이 오른쪽, 위쪽
                        return False
                    return True

        if t == 2:
            ny = y + dy[t][idx]
            if 0 <= ny < R:
                temp_walls = wall_board[ny][x]
                if idx == 0:  # 대각선 위
                    if temp_walls[2] or temp_walls[4]:  # 벽이 왼쪽, 아래쪽
                        return False
                    return True
                elif idx == 2:  # 대각선 아래
                    if temp_walls[2] or temp_walls[3]:  # 벽이 왼쪽, 위쪽
                        return False
                    return True

        if t == 3:
            nx = x + dx[t][idx]
            if 0 <= nx < C:
                temp_walls = wall_board[y][nx]
                if idx == 0:  # 대각선 왼쪽
                    if temp_walls[3] or temp_walls[1]:  # 벽이 위쪽, 오른쪽
                        return False
                    return True
                elif idx == 2:  # 대각선 오른쪽
                    if temp_walls[3] or temp_walls[2]:  # 벽이 위쪽, 왼쪽
                        return False
                    return True

        if t == 4:
            nx = x + dx[t][idx]
            if 0 <= nx < C:
                temp_walls = wall_board[y][nx]
                if idx == 0:  # 대각선 왼쪽
                    if temp_walls[4] or temp_walls[1]:  # 벽이 아래쪽, 오른쪽
                        return False
                    return True
                elif idx == 2:  # 대각선 오른쪽
                    if temp_walls[4] or temp_walls[2]:  # 벽이 아래쪽, 왼쪽
                        return False
                    return True

        return False

    def init_heater():
        add_heat = [[0] * C for _ in range(R)]
        for y, x, t in heater:
            y += dy[t][1]
            x += dx[t][1]
            if not isin(y, x):
                continue

            q = deque()
            q.append([y, x, 4])

            global visited
            visited = [[0] * C for _ in range(R)]
            visited[y][x] = 1
            add_heat[y][x] += 5

            while q:
                y, x, cnt = q.popleft()
                for idx, (dy1, dx1) in enumerate(zip(dy[t], dx[t])):
                    if 0 < cnt and isnext(y, x, t, idx):
                        ny, nx = y + dy1, x + dx1
                        if isin(ny, nx) and visited[ny][nx] == 0:
                            add_heat[ny][nx] += cnt

                            q.append([ny, nx, cnt - 1])
                            visited[ny][nx] = 1

        return add_heat

    def update_heat():
        global add_heat
        for i in range(R):
            for j in range(C):
                board[i][j] += add_heat[i][j]

    def minus_one():
        for i in range(R):
            if board[i][0] != 0:
                board[i][0] -= 1
            if board[i][-1] != 0:
                board[i][-1] -= 1

        for j in range(1, C - 1):
            if board[0][j] != 0:
                board[0][j] -= 1
            if board[-1][j] != 0:
                board[-1][j] -= 1

    def spread_heat():
        heats = [[0] * C for _ in range(R)]
        for y in range(R):
            ny = y + 1
            for x in range(C):
                nx = x + 1
                if isin(ny, x) and not wall_board[ny][x][3]:  # 상 (위쪽 벽 없음)
                    sub = abs(board[ny][x] - board[y][x]) // 4
                    if board[ny][x] > board[y][x]:
                        heats[ny][x] -= sub
                        heats[y][x] += sub
                    else:
                        heats[ny][x] += sub
                        heats[y][x] -= sub

                if isin(y, nx) and not wall_board[y][x][1]:  # 우 (오른쪽 벽 없음)
                    sub = abs(board[y][nx] - board[y][x]) // 4
                    if board[y][nx] > board[y][x]:
                        heats[y][nx] -= sub
                        heats[y][x] += sub
                    else:
                        heats[y][nx] += sub
                        heats[y][x] -= sub

        for y in range(R):
            for x in range(C):
                board[y][x] += heats[y][x]

        minus_one()

    def check():
        for y, x in check_pos:
            if board[y][x] < K:
                return False
        return True

    global visited
    visited = [[0] * C for _ in range(R)]
    cnt = 1

    global add_heat
    add_heat = init_heater()
    # for h in add_heat:
    #     print(h)
    # print()

    while cnt <= 100:
        update_heat()
        spread_heat()
        if check():
            break
        cnt += 1

    # for b in board:
    #     print(b)
    # print()

    return cnt


if __name__ == "__main__":
    print(solution())
