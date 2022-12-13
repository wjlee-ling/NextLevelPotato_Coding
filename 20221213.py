# 효율성까지 통과하려면 이분탐색을 사용해야 함


def solution(stones, k):
    """
    Args:
        stones : 디딤돌에 적힌 숫자가 순서대로 담긴 배열
        k : 한번에 건너뛸 수 있는 디딤돌의 최대 칸수
    Returns:
        최대 몇 명까지 징검다리를 건널 수 있는 사람 수
    """
    left = 1
    right = max(stones)
    
    while left <= right:
        cnt = 0
        mid = (left + right) // 2 # mid == 통과하는 사람 수
        
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k: # cnt가 k개 이상이면 디딤돌을 건널 수 없음
                break
        
        if cnt >= k: # 디딤돌을 건널 수 없으므로 통과하는 사람 수를 줄여봄
            right = mid - 1
        elif cnt < k: # 디딤돌을 건널 수 있으므로 left 값 + 1
            left = mid + 1
    
    return left

# ----------------------------------------------

# test1. 시간초과 / test21. 실패
# 효율성 fail

# 0이 k개 이상 붙어 있으면 안된다.
# k개 범위의 슬라이딩 윈도우로 합이 0이 되면 종료

def solution(stones, k):
    """
    Args:
        stones : 디딤돌에 적힌 숫자가 순서대로 담긴 배열
        k : 한번에 건너뛸 수 있는 디딤돌의 최대 칸수
    Returns:
        최대 몇 명까지 징검다리를 건널 수 있는 사람 수
    """
    answer = 0
    window = sum(stones[:k])
    if window == 0:
        return answer
    answer += 1
    
    while True:
        stones = [stones[i] - 1 if stones[i] > 0 else 0 for i in range(len(stones))]

        for i in range(k, len(stones)-k+1):
            window = sum(stones[i:i+k])
            if window == 0:
                return answer
        
        answer += 1
    
    return answer