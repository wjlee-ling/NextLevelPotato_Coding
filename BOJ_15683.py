def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    global answer
    answer = N * M

    cctvs = []
    for i in range(N):
        for j in range(M):
            if 1 <= board[i][j] <= 5:
                cctvs.append((board[i][j], i, j))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    mode = [
        [],
        [[0], [1], [2], [3]],
        [[0, 1], [2, 3]],
        [[0, 3], [1, 3], [1, 2], [0, 2]],
        [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]],
        [[0, 1, 2, 3]],
    ]

    def watch(board, mode, row, col):
        for d in mode:
            nrow = row
            ncol = col

            while True:
                nrow += dy[d]
                ncol += dx[d]
                if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M:
                    break

                if board[nrow][ncol] == 6:
                    break

                if board[nrow][ncol] == 0:
                    board[nrow][ncol] = 7

    def dfs(cnt, arr):
        global answer

        if cnt == len(cctvs):
            result = 0
            for i in range(N):
                result += arr[i].count(0)
            # if answer > result:
            #     for a in arr:
            #         print(a)
            #     print()
            answer = min(answer, result)
            return

        temp = [a[:] for a in arr]
        cctv_num, row, col = cctvs[cnt]
        for m in mode[cctv_num]:
            watch(temp, m, row, col)
            dfs(cnt + 1, temp)
            temp = [a[:] for a in arr]

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
