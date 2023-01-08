"""
프로그래머스
디펜스 게임
https://school.programmers.co.kr/learn/courses/30/lessons/142085

solved
"""

from heapq import heappop, heappush


def solution(n, k, enemy):
    answer = 0

    defensed_enemy = []
    n_enemy = 0
    for e in enemy:
        heappush(defensed_enemy, -e)
        n_enemy += e
        if n < n_enemy:
            if k <= 0:
                break
            n_enemy += heappop(defensed_enemy)
            k -= 1
        answer += 1

    return answer


if __name__ == "__main__":
    nums = [7, 2]
    ks = [3, 4]
    enemies = [[4, 2, 4, 5, 3, 3, 1], [3, 3, 3, 3]]
    result = [5, 4]
    for n, k, enemy in zip(nums, ks, enemies):
        print(solution(n, k, enemy))
