# Programmers 43238: 입국심사

# 시간의 최소 ~ 최대 범위를 탐색 범위로 설정, 중간 값이 n명을 심사할 수 있는 시간인지 탐색
# left, right가 같아질 때 까지 while 문 안에서 탐색
## 중간 값의 심사할 수 있는 사람 수 계산
### `n`명보다 많을 경우 왼쪽 범위 탐색
### `n`명보다 적을 경우 오른쪽 범위 탐색


def solution(n, times):
    """
    Args:
        n (int) : 입국심사를 기다리는 사람 수
        times (List(int)) : 각 심사관이 한 명을 심사하는데 걸리는 시간이 담기는 배열
    Returns:
        모든 사람이 심사를 받는데 걸리는 시간의 최솟값
    """
    answer = 0

    # 이진 탐색을 위한 범위 설정
    times = sorted(times)
    left, right = times[0], times[-1]*n # right = 가장 심사시간이 긴 심사관에게 n명이 모두 심사받는 경우

    while left <= right:
        mid = (left + right) // 2
        mid_n = 0

        for time in times:
            mid_n += mid // time # 각 심사관마다 mid분 동안 심사할 수 있는 사람 수를 더해줌
            # 모든 심사관들을 거치지 않더라도 n명 이상의 심사를 할 수 있다면 반복문 탈출
            if mid_n >= n:
                break

        if mid_n >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer