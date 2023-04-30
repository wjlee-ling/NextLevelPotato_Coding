def solution():
    global answer
    answer = 0
    # fmt:off
    score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
    graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
    # fmt:on

    dice = list(map(int, input().split()))

    def backtracking(cnt, total, horse, test):
        global answer
        if cnt >= len(dice):
            answer = max(answer, total)
            return

        for i in range(4):
            idx = horse[i]
            if len(graph[idx]) == 2:
                idx = graph[idx][1]
            else:
                idx = graph[idx][0]

            for _ in range(1, dice[cnt]):
                idx = graph[idx][0]

            if idx == 32 or (idx < 32 and idx not in horse):
                temp = horse[i]
                horse[i] = idx
                test.append(idx)
                backtracking(cnt + 1, total + score[idx], horse, test)
                test.pop()
                horse[i] = temp

    backtracking(0, 0, [0, 0, 0, 0], [])

    return answer


if __name__ == "__main__":
    print(solution())
