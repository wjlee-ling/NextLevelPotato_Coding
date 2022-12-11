import copy
from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    # print((sum(queue1) + sum(queue2)))
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1

    temp1 = copy.deepcopy(queue1)
    temp2 = copy.deepcopy(queue2)
    while sum(queue1) != sum(queue2):
        if sum(queue1) >= sum(queue2):
            queue2.append(queue1.popleft())
        else:
            queue1.append(queue2.popleft())
        # print(queue1, queue2)
        answer += 1

        if temp1 == queue1 or temp2 == queue2:
            return -1

    return answer


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
