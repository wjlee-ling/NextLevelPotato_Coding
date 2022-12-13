"""
efficiency test fail
"""


def solution(board):
    answer = 0

    n, m = len(board), len(board[0])
    target = min(n, m)
    # print("@", n, m, target)
    for t in range(target, 0, -1):
        for r in range(n - t + 1):
            for c in range(m - t + 1):
                # print("#", r, c)
                if board[r][c] == 1:
                    # print("@@", r, c, i)
                    answer = max(answer, rect(board, r, c, t))
                    if answer:
                        return answer

    return answer


def rect(board, row, col, n):
    cnt = 0
    for r in range(n):
        for c in range(n):
            nrow = row + r
            ncol = col + c
            if 0 <= nrow < len(board) and 0 <= ncol < len(board[0]) and board[nrow][ncol] == 1:
                # print("@@@", nrow, ncol)
                cnt += 1

    if cnt == n * n:
        return n * n

    return 0


if __name__ == "__main__":
    board = [
        [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]],
        [[0, 0, 1, 1], [1, 1, 1, 1]],
    ]
    answer = [9, 4]

    for b in board:
        print(solution(b))
