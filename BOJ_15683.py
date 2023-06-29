"""
15683. 감시
"""


def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    global answer
    answer = float("inf")

    # 상좌하우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    modes = [
        [],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]],
    ]

    def check(board):
        result = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    result += 1

        return result

    def is_valid(y, x):
        if 0 <= y < N and 0 <= x < M:
            return True
        return False

    cctvs = []
    for y in range(N):
        for x in range(M):
            if 1 <= board[y][x] <= 5:
                cctvs.append([board[y][x], y, x])

    def watch(board, mode, y, x):
        for d in mode:
            ny = y
            nx = x
            while True:
                ny += dy[d]
                nx += dx[d]

                if not is_valid(ny, nx) or board[ny][nx] == 6:
                    break

                board[ny][nx] = 7

    def dfs(cnt, board):
        global answer
        if cnt == len(cctvs):
            answer = min(answer, check(board))
            return

        temp = [b[:] for b in board]
        cctv_num, y, x = cctvs[cnt]
        for mode in modes[cctv_num]:
            watch(temp, mode, y, x)
            dfs(cnt + 1, temp)
            temp = [b[:] for b in board]

    dfs(0, board)
    print(answer)


if __name__ == "__main__":
    solution()


"""
상하좌우
03, 13, 12, 02
상우, 우하, 좌하, 좌상

023, 013, 123, 012
상우좌, 상우하, 우하좌, 하좌상
"""
