"""
14888. 연산자 끼워넣기
"""


def solution():
    N = int(input())
    A = list(map(int, input().split()))
    opers = list(map(int, input().split()))

    global max_total, min_total
    max_total = 0
    min_total = float("inf")

    def solve(cnt, total, plus, minus, multiply, divide):
        global max_total, min_total

        if cnt == N:
            max_total = max(max_total, total)
            min_total = min(min_total, total)

        if plus:
            solve(cnt + 1, total + A[cnt], plus - 1, minus, multiply, divide)
        if minus:
            solve(cnt + 1, total - A[cnt], plus, minus - 1, multiply, divide)
        if multiply:
            solve(cnt + 1, total * A[cnt], plus, minus, multiply - 1, divide)
        if divide:
            solve(cnt + 1, int(total / A[cnt]), plus, minus, multiply, divide - 1)

    solve(1, A[0], opers[0], opers[1], opers[2], opers[3])

    print(max_total)
    print(min_total)


if __name__ == "__main__":
    solution()
