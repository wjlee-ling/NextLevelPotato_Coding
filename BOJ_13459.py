from collections import deque


def solution():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    # for b in board:
    #     print(b)
    # print()

    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for y in range(N):
        for x in range(M):
            if board[y][x] == "R":
                red = [y, x]
            if board[y][x] == "B":
                blue = [y, x]
            if board[y][x] == "O":
                out = [y, x]

    q = deque()
    q.append([*red, *blue, 0])
    # print(q)
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]  # visited[ry][rx][by][bx]
    visited[red[0]][red[1]][blue[0]][blue[1]] = 1
    # print(visited)

    def isin(y, x):
        if 0 <= y < N and 0 <= x < M and board[y][x] != "#":
            return True
        return False

    def move(y, x, d):
        cnt = 0
        while isin(y, x):
            y = y + dy[d]
            x = x + dx[d]
            cnt += 1

            if y == out[0] and x == out[1]:
                return (y, x, cnt)

        return (y - dy[d], x - dx[d], cnt - 1)

    while q:
        ry, rx, by, bx, cnt = q.popleft()
        if cnt >= 10:  # bfs 탐색에서 10번을 초과하는 경우가 나오면 이후 탐색에서도 10번 초과이기 때문에 바로 return
            return -1

        for d in range(4):
            nry, nrx, rcnt = move(ry, rx, d)
            nby, nbx, bcnt = move(by, bx, d)

            if nby == out[0] and nbx == out[1]:  # 파란 구슬이 구멍에 빠지면 continue
                continue

            if nry == out[0] and nrx == out[1]:  # 빨간 구슬이 구멍에 빠지면 종료
                return cnt + 1

            if nry == nby and nrx == nbx:  # 빨간 구슬과 파란 구슬의 위치가 같다면
                if rcnt > bcnt:  # 빨간 구슬이 더 많이 움직였다면 빨간 구슬을 반대방향으로 한 칸 이동
                    nry -= dy[d]
                    nrx -= dx[d]
                    rcnt -= 1
                elif rcnt < bcnt:  # 파란 구슬이 더 많이 움직였다면 파란 구슬을 반대방향으로 한 칸 이동
                    nby -= dy[d]
                    nbx -= dx[d]
                    bcnt -= 1

            # print("@", d)
            # print(f"{nry},{nrx},{rcnt} / {nby},{nbx},{bcnt}")
            # print()

            if visited[nry][nrx][nby][nbx] == 0:
                visited[nry][nrx][nby][nbx] = 1
                q.append([nry, nrx, nby, nbx, cnt + 1])

    return -1


if __name__ == "__main__":
    print(solution())
