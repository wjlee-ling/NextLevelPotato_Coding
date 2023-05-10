"""
모노미노도미노 2
"""


def solution():
    N = int(input())
    global answer
    answer = 0

    green_board = [[0] * 4 for _ in range(6)]
    blue_board = [[0] * 6 for _ in range(4)]

    def check_blue():
        global answer

        for col in range(2, 6):
            cnt = 0
            for row in range(4):
                if blue_board[row][col]:
                    cnt += 1

            if cnt == 4:
                remove_blue(col)
                answer += 1

    def check_green():
        global answer

        for row in range(2, 6):
            cnt = 0
            for col in range(4):
                if green_board[row][col]:
                    cnt += 1

            if cnt == 4:
                remove_green(row)
                answer += 1

    def remove_blue(idx):
        for col in range(idx, 0, -1):
            for row in range(4):
                blue_board[row][col] = blue_board[row][col - 1]

        for row in range(4):
            blue_board[row][0] = 0

    def remove_green(idx):
        for row in range(idx, 0, -1):
            for col in range(4):
                green_board[row][col] = green_board[row - 1][col]

        for col in range(4):
            green_board[0][col] = 0

    def move_blue(t, x):
        y = 1
        if t == 1 or t == 2:
            while True:
                if y + 1 > 5 or blue_board[x][y + 1]:
                    blue_board[x][y] = 1
                    if t == 2:
                        blue_board[x][y - 1] = 1
                    break
                y += 1

        else:
            while True:
                if y + 1 > 5 or blue_board[x][y + 1] != 0 or blue_board[x + 1][y + 1] != 0:
                    blue_board[x][y], blue_board[x + 1][y] = 1, 1
                    break
                y += 1

        check_blue()

        for col in range(2):
            for row in range(4):
                if blue_board[row][col]:
                    remove_blue(5)
                    break

    def move_green(t, y):
        x = 1
        if t == 1 or t == 3:
            while True:
                if x + 1 > 5 or green_board[x + 1][y]:
                    green_board[x][y] = 1
                    if t == 3:
                        green_board[x - 1][y] = 1
                    break
                x += 1

        else:
            while True:
                if x + 1 > 5 or green_board[x + 1][y] != 0 or green_board[x + 1][y + 1] != 0:
                    green_board[x][y], green_board[x][y + 1] = 1, 1
                    break
                x += 1

        check_green()

        for row in range(2):
            for col in range(4):
                if green_board[row][col]:
                    remove_green(5)
                    break

    for _ in range(N):
        t, x, y = map(int, input().split())

        move_blue(t, x)
        move_green(t, y)

    cnt_b = 0
    cnt_g = 0
    for i in range(4):
        for j in range(2, 6):
            if blue_board[i][j]:
                cnt_b += 1

    for i in range(2, 6):
        for j in range(4):
            if green_board[i][j]:
                cnt_g += 1

    print(answer)
    print(cnt_b + cnt_g)


if __name__ == "__main__":
    solution()
