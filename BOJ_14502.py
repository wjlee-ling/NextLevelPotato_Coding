"""
연구소

7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""
from collections import deque


def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    global answer
    answer = 0

    def bfs():
        global answer
        q = deque()
        for r in range(N):
            for c in range(M):
                if board[r][c] == 2:
                    q.append([r, c])

        temp_board = [b[:] for b in board]

        while q:
            row, col = q.popleft()

            for d in range(4):
                nrow = row + dy[d]
                ncol = col + dx[d]

                if 0 <= nrow < N and 0 <= ncol < M and temp_board[nrow][ncol] == 0:
                    temp_board[nrow][ncol] = 2
                    q.append([nrow, ncol])

        result = 0
        for r in range(N):
            result += temp_board[r].count(0)

        answer = max(answer, result)

    def add_wall(cnt):
        if cnt == 3:
            bfs()
            return

        for r in range(N):
            for c in range(M):
                if board[r][c] == 0:
                    board[r][c] = 1
                    add_wall(cnt + 1)
                    board[r][c] = 0

    add_wall(0)
    print(answer)


if __name__ == "__main__":
    solution()
