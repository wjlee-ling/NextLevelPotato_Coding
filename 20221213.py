"""
solved
"""


def solution(stones, k):
    answer = 0
    left = min(stones)
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


if __name__ == "__main__":
    stones = [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]]
    k = [3]
    result = 3

    for stone, num in zip(stones, k):
        print(solution(stone, num))
