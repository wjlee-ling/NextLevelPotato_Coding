"""
12100. 2048 (Easy)
"""


from collections import deque
from copy import deepcopy


def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    global answer
    answer = 0

    # for b in board:
    #     print(b)
    # print()

    def check(board):
        result = 0
        for y in range(N):
            result = max(max(board[y]), result)

        return result

    # 이동과 병합
    def move_merge(board, d):
        temp_board = [[0] * N for _ in range(N)]

        # 상
        if d == 0:
            for x in range(N):
                q = deque()
                for y in range(N):
                    if board[y][x] == 0:
                        continue
                    q.append(board[y][x])

                y = 0
                while q:
                    num = q.popleft()
                    if temp_board[y][x] == 0:
                        temp_board[y][x] = num
                    elif temp_board[y][x] == num:
                        temp_board[y][x] += num
                        y += 1
                    elif temp_board[y][x] != num:
                        y += 1
                        temp_board[y][x] = num
        # 하
        elif d == 1:
            for x in range(N):
                q = deque()
                for y in range(N - 1, -1, -1):
                    if board[y][x] == 0:
                        continue
                    q.append(board[y][x])

                y = N - 1
                while q:
                    num = q.popleft()
                    if temp_board[y][x] == 0:
                        temp_board[y][x] = num
                    elif temp_board[y][x] == num:
                        temp_board[y][x] += num
                        y -= 1
                    elif temp_board[y][x] != num:
                        y -= 1
                        temp_board[y][x] = num
        # 좌
        elif d == 2:
            for y in range(N):
                q = deque()
                for x in range(N):
                    if board[y][x] == 0:
                        continue
                    q.append(board[y][x])

                x = 0
                while q:
                    num = q.popleft()
                    if temp_board[y][x] == 0:
                        temp_board[y][x] = num
                    elif temp_board[y][x] == num:
                        temp_board[y][x] += num
                        x += 1
                    elif temp_board[y][x] != num:
                        x += 1
                        temp_board[y][x] = num
        # 우
        elif d == 3:
            for y in range(N):
                q = deque()
                for x in range(N - 1, -1, -1):
                    if board[y][x] == 0:
                        continue
                    q.append(board[y][x])

                x = N - 1
                while q:
                    num = q.popleft()
                    if temp_board[y][x] == 0:
                        temp_board[y][x] = num
                    elif temp_board[y][x] == num:
                        temp_board[y][x] += num
                        x -= 1
                    elif temp_board[y][x] != num:
                        x -= 1
                        temp_board[y][x] = num

        return temp_board

    # board = move_merge(1)
    # for b in board:
    #     print(b)
    # print()

    def dfs(board, cnt):
        global answer
        if cnt >= 5:
            result = check(board)
            answer = max(answer, result)
            return

        temp_board = deepcopy(board)
        for d in range(4):
            result_board = move_merge(temp_board, d)

            # for r in result_board:
            #     print(r)
            # print()

            dfs(result_board, cnt + 1)

    dfs(board, 0)
    print(answer)

    return


if __name__ == "__main__":
    solution()
