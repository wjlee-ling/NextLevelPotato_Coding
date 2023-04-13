"""
로봇 청소기
"""

from collections import deque


def solution():
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())

    # 북동남서
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    board = [list(map(int, input().split())) for _ in range(N)]

    q = deque()
    q.append([r, c, d])
    answer = 2

    while q:
        row, col, d = q.popleft()
        flag = True  # 청소되지 않은 빈 칸이 없다면 True
        board[row][col] = answer

        for i in range(1, 5):  # 주변 4칸 중 청소
            nd = (d - 1 * i) % 4
            nrow = row + dy[nd]
            ncol = col + dx[nd]
            if 0 <= nrow < N and 0 <= ncol < M and board[nrow][ncol] == 0:
                answer += 1
                q.append([nrow, ncol, nd])
                flag = False
                break

        if flag:  # 후진
            nrow = row - dy[d]
            ncol = col - dx[d]
            if 0 <= nrow < N and 0 <= ncol < M and board[nrow][ncol] != 1:
                q.append([nrow, ncol, d])
            else:
                break

        # for b in board:
        #     print(b)
        # print()

    print(answer - 1)


if __name__ == "__main__":
    solution()
