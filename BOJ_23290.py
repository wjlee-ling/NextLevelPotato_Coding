"""
23290. 마법사 상어와 복제
"""


from collections import deque
from copy import deepcopy


def solution():
    M, S = map(int, input().split())
    global board
    board = [[deque() for _ in range(4)] for _ in range(4)]

    for _ in range(M):
        fy, fx, d = map(int, input().split())
        board[fy - 1][fx - 1].append(d - 1)  # 물고기는 0~7로(방향) 표시

    # 상어 위치
    global sy, sx
    sy, sx = map(int, input().split())
    sy -= 1
    sx -= 1

    # 물고기 이동방향
    fdy = [0, -1, -1, -1, 0, 1, 1, 1]
    fdx = [-1, -1, 0, 1, 1, 1, 0, -1]

    # 상어 이동방향
    sdy = [-1, 0, 1, 0]
    sdx = [0, -1, 0, 1]

    # for b in board:
    #     print(b)
    # print()

    smell_board = [[0] * 4 for _ in range(4)]

    def isin(y, x):
        if 0 <= y < 4 and 0 <= x < 4:
            return True
        return False

    def move_fish(t):
        global board
        move_board = [[deque() for _ in range(4)] for _ in range(4)]

        for y in range(4):
            for x in range(4):
                if board[y][x]:
                    fish = board[y][x]
                    length = len(fish)
                    for _ in range(length):
                        d = fish.popleft()
                        nd = d
                        flag = True
                        for i in range(8):
                            nd = (d - i) % 8
                            ny = y + fdy[nd]
                            nx = x + fdx[nd]
                            # (smell_board[ny][nx] == 0 or smell_board[ny][nx] + 2 < t) : 물고기 냄새가 사라졌는지 체크
                            if isin(ny, nx):
                                if (smell_board[ny][nx] == 0 or smell_board[ny][nx] + 2 < t) and not (ny == sy and nx == sx):
                                    move_board[ny][nx].append(nd)
                                    flag = False
                                    break
                        if flag:
                            move_board[y][x].append(d)
        # print(sy, sx)
        # print("@move board")
        # for m in move_board:
        #     print(m)
        # print()

        # print("@smell board")
        # for s in smell_board:
        #     print(s)
        # print()

        board = deepcopy(move_board)

    def move_shark(t):
        global sy, sx
        # q = deque()
        # q.append([sy, sx, 0, "", 0])  # y, x, 이동횟수, 이동방향, 물고기 수
        # visited = [[0] * 4 for _ in range(4)]
        # visited[sy][sx] = 1

        # moves = []
        # while q:
        #     y, x, cnt, dirs, n_fish = q.popleft()
        #     if cnt == 3:
        #         moves.append([y, x, int(dirs), n_fish])
        #         continue
        #     for d in range(4):
        #         ny = y + sdy[d]
        #         nx = x + sdx[d]
        #         if isin(ny, nx) and visited[ny][nx] == 0:
        #             print("@@@@", ny, nx, len(board[ny][nx]), d + 1)
        #             q.append([ny, nx, cnt + 1, dirs + str(d + 1), n_fish + len(board[ny][nx])])
        #             visited[ny][nx] = 1

        moves = []
        visited = [[0] * 4 for _ in range(4)]

        def dfs(y, x, cnt, dirs, n_fish):
            if cnt == 3:
                moves.append([y, x, int(dirs), n_fish])
                return

            for d in range(4):
                ny = y + sdy[d]
                nx = x + sdx[d]
                if isin(ny, nx):
                    if visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        dfs(ny, nx, cnt + 1, dirs + str(d + 1), n_fish + len(board[ny][nx]))
                        visited[ny][nx] = 0
                    else:  # 방문했던 방향이라면 물고기 카운트를 그대로
                        dfs(ny, nx, cnt + 1, dirs + str(d + 1), n_fish)

        dfs(sy, sx, 0, "", 0)
        result = sorted(moves, key=lambda x: (-x[3], x[2]))
        # print(result)

        # 상어가 이동한 경로의 물고기들 제거
        directions = str(result[0][2])
        y = sy
        x = sx
        for d in directions:
            d = int(d) - 1
            ny = y + sdy[d]
            nx = x + sdx[d]
            if isin(ny, nx) and board[ny][nx]:
                board[ny][nx] = deque()
                # 물고기 냄새 남기기
                smell_board[ny][nx] = t
            y = ny
            x = nx

        # 상어 위치 갱신
        sy = result[0][0]
        sx = result[0][1]

    for t in range(1, S + 1):
        # 복제 마법 시전 (board 복사)
        temp_board = deepcopy(board)

        # 물고기 이동
        move_fish(t)
        # print("@fish move")
        # for b in board:
        #     print(b)
        # print()

        # 상어 이동
        move_shark(t)

        # 복제 마법
        for y in range(4):
            for x in range(4):
                board[y][x].extend(temp_board[y][x])

        # print("@smell board")
        # for s in smell_board:
        #     print(s)
        # print()

        # print(t, sy, sx)
        # for b in board:
        #     print(b)
        # print()

    answer = 0
    for y in range(4):
        for x in range(4):
            answer += len(board[y][x])
    return answer


if __name__ == "__main__":
    print(solution())
