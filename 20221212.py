"""
solved
"""


def solution(queue1, queue2):
    answer = 0
    q = queue1 + queue2
    target = sum(q) // 2

    i, j = 0, len(queue1) - 1
    cur = sum(queue1)

    while i < len(q) and j < len(q):
        if cur == target:
            return answer
        elif cur < target and j < len(q) - 1:
            j += 1
            cur += q[j]
        else:
            cur -= q[i]
            i += 1

        answer += 1

    return -1


if __name__ == "__main__":
    queue1 = [
        [3, 2, 7, 2],
        [1, 2, 1, 2],
        [1, 1],
    ]
    queue2 = [
        [4, 6, 5, 1],
        [1, 10, 1, 2],
        [1, 5],
    ]
    results = [2, 7, -1]

    for q1, q2 in zip(queue1, queue2):
        print(solution(q1, q2))
