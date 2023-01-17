"""
프로그래머스
귤 고르기
https://school.programmers.co.kr/learn/courses/30/lessons/138476

solved
"""

from collections import Counter


def solution(k, tangerine):
    answer = 0

    for t, n in Counter(tangerine).most_common():
        if k > 0:
            k -= n
            answer += 1

    return answer


if __name__ == "__main__":
    ks = [6, 4, 2]
    tangerine = [[1, 3, 2, 5, 4, 5, 2, 3], [1, 3, 2, 5, 4, 5, 2, 3], [1, 1, 1, 1, 2, 2, 2, 3]]
    result = [3, 2, 1]
    for k, t in zip(ks, tangerine):
        print(solution(k, t))
