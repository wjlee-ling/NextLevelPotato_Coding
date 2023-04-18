"""
사다리 조작
"""


def solution():
    N, M, H = map(int, input().split())
    if M == 0:
        return 0

    global answer
    answer = 4
    board = [[0] * (N) for _ in range(H)]

    for _ in range(M):
        r, c = map(int, input().split())
        board[r - 1][c - 1] = 1

    def check():
        for col in range(N):
            c = col
            for r in range(H):
                if board[r][c]:
                    c += 1
                elif c > 0 and board[r][c - 1]:  # 왼쪽 체크
                    c -= 1

            if c != col:
                return False
        return True

    def dfs(row, col, cnt):
        global answer
        if check():
            answer = min(answer, cnt)
            return

        if cnt == 3 or cnt >= answer:
            return

        for r in range(row, H):
            if r == row:
                k = col
            else:
                k = 0
            # k = col if r == row else 0
            for c in range(k, N - 1):
                if board[r][c] == 0 and board[r][c + 1] == 0:
                    board[r][c] = 1
                    dfs(r, c + 2, cnt + 1)
                    board[r][c] = 0

    dfs(0, 0, 0)

    if answer < 4:
        return answer
    else:
        return -1


if __name__ == "__main__":
    print(solution())
