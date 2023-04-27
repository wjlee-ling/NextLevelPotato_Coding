"""
게리멘더링 2
"""


def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    def solve(x, y, d1, d2):
        x -= 1
        y -= 1

        temp_board = [[0] * N for _ in range(N)]
        for d in range(d1 + 1):
            nx = x + d
            ny = y - d
            if 0 <= nx < N and 0 <= ny < N:
                temp_board[nx][ny] = 5

        for d in range(d2 + 1):
            nx = x + d
            ny = y + d
            if 0 <= nx < N and 0 <= ny < N:
                temp_board[nx][ny] = 5

        for d in range(d2 + 1):
            nx = x + d1 + d
            ny = y - d1 + d
            if 0 <= nx < N and 0 <= ny < N:
                temp_board[nx][ny] = 5

        for d in range(d1 + 1):
            nx = x + d2 + d
            ny = y + d2 - d
            if 0 <= nx < N and 0 <= ny < N:
                temp_board[nx][ny] = 5

        for r in range(N):
            flag = False
            for c in range(N):
                if temp_board[r][c] == 5:
                    if flag:
                        for j in range(c1, c + 1):
                            temp_board[r][j] = 5
                    else:
                        flag = True
                        c1 = c

        # 1번 선거구
        for r in range(x + d1):
            for c in range(y + 1):
                if temp_board[r][c] == 0:
                    temp_board[r][c] = 1

        # 2번 선거구
        for r in range(x + d2 + 1):
            for c in range(y, N):
                if temp_board[r][c] == 0:
                    temp_board[r][c] = 2

        # 3번 선거구
        for r in range(x + d1, N):
            for c in range(y - d1 + d2):
                if temp_board[r][c] == 0:
                    temp_board[r][c] = 3

        # 4번 선거구
        for r in range(x + d2, N):
            for c in range(y - d1 + d2, N):
                if temp_board[r][c] == 0:
                    temp_board[r][c] = 4

        for t in temp_board:
            print(t)
        print()

        populations = [0] * 5
        for r in range(N):
            for c in range(N):
                num = temp_board[r][c]
                populations[num - 1] += board[r][c]

        result = max(populations) - min(populations)
        return result

    answer = float("inf")
    for r in range(N):
        for c in range(N):
            for d1 in range(N):
                for d2 in range(N):
                    if r + d1 >= N or r + d2 >= N or c - d1 + d2 >= N:
                        continue
                    answer = min(answer, solve(r, c, d1, d2))

    return answer


if __name__ == "__main__":
    print(solution())
