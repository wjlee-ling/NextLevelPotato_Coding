"""
퇴사
"""


def solution():
    N = int(input())
    consults = [list(map(int, input().split())) for _ in range(N)]

    # print(consults)

    global answer
    answer = 0

    def solve(now, end, pay, pays):
        global answer
        if now == N:
            answer = max(answer, pay)
            print(pay, pays)
            return

        if now > end and consults[now][0] <= N - now:
            pays.append([now + 1, end + consults[now][0] + 1, pay + consults[now][1]])
            solve(now + 1, end + consults[now][0], pay + consults[now][1], pays[:])
            pays.pop()
            solve(now + 1, now, pay, pays[:])
        else:
            solve(now + 1, end, pay, pays[:])

    solve(0, -1, 0, [])
    print(answer)


if __name__ == "__main__":
    solution()
