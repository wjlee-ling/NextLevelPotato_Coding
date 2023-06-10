"""
테트로미노
"""


def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    global answer
    answer = 0
    max_val = max(map(max, board))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = [[0] * M for _ in range(N)]

    def is_valid(y, x):
        if 0 <= y < N and 0 <= x < M:
            return True
        return False

    def dfs(y, x, cnt, total):
        global answer
        if answer >= total + max_val * (4 - cnt):
            return

        if cnt == 4:
            answer = max(answer, total)
            return

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if is_valid(ny, nx) and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                dfs(ny, nx, cnt + 1, total + board[ny][nx])
                visited[ny][nx] = 0
                if cnt == 2:  # ㅗ, ㅜ, ㅓ, ㅏ 모양
                    visited[ny][nx] = 1
                    dfs(y, x, cnt + 1, total + board[ny][nx])
                    visited[ny][nx] = 0

    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            dfs(i, j, 1, board[i][j])
            visited[i][j] = 0

    return answer


if __name__ == "__main__":
    print(solution())
