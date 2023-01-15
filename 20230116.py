"""
프로그래머스
도둑질
https://school.programmers.co.kr/learn/courses/30/lessons/42897

solved
"""


def solution(money):
    answer = 0

    # 첫 번째 집을 터는 경우
    dp1 = [0 for _ in range(len(money))]
    dp1[0] = money[0]
    dp1[1] = money[0]
    # print(dp1)

    for i in range(2, len(dp1) - 1):  # 첫 번째 집을 털면 마지막 집은 털지 못함
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])
    # print(dp1)

    # 첫 번째 집을 털지 않는 경우
    dp2 = [0 for _ in range(len(money))]
    dp2[1] = money[1]
    # print(dp2)

    for i in range(2, len(dp2)):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])
    # print(dp2)

    return max(max(dp1), max(dp2))


if __name__ == "__main__":
    money = [
        [1, 2, 3, 1],
    ]
    result = [4]
    for m in money:
        print(solution(m))
