"""
14502. 연구소
python3 시간초과
pypy3 통과
"""

from collections import deque


def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    global answer
    answer = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def check(board):
        global answer

        total = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    total += 1

        answer = max(answer, total)

    def add_wall(cnt):
        if cnt == 3:
            bfs()
            return

        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    add_wall(cnt + 1)
                    board[i][j] = 0

    def is_valid(y, x):
        if 0 <= y < N and 0 <= x < M:
            return True
        return False

    def bfs():
        global answer

        q = deque()
        for i in range(N):
            for j in range(M):
                if board[i][j] == 2:
                    q.append([i, j])

        temp_board = [b[:] for b in board]
        while q:
            y, x = q.popleft()

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if is_valid(ny, nx) and temp_board[ny][nx] == 0:
                    temp_board[ny][nx] = 2
                    q.append([ny, nx])

        # for t in temp_board:
        #     print(t)
        # print()

        check(temp_board)

    add_wall(0)
    print(answer)


if __name__ == "__main__":
    solution()
