"""
solved
"""


from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    max_gap = -1

    for comb in combinations_with_replacement(range(11), n):
        temp = [0] * 11

        for i in comb:
            temp[10 - i] += 1

        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == temp[idx] == 0:
                continue
            elif info[idx] >= temp[idx]:
                apeach += 10 - idx
            else:
                lion += 10 - idx

        if lion > apeach:
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = temp
    return answer


if __name__ == "__main__":
    nums = [5, 1, 9, 10]
    infos = [
        [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3],
    ]
    results = [
        [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0],
        [-1],
        [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2],
    ]

    for n, info in zip(nums, infos):
        print(solution(n, info))
