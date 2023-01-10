# 남은 병사의 수보다 현재 라운드의 적의 수가 더 많으면 게임 종료
# '무적권' 스킬: 병사 소모 없이 한 라운드의 공격을 막을 수 있다. (k번 사용 가능)


# ❌ fail : 시간초과도 있고 실패도 있음
# 우선 큰 값들을 무적권으로 막아야 할듯
## k개까지의 큰 값들의 idx를 따로 저장해서
## 하나씩 pop 해가지고 병사나 남지 않을 떄 까지

from collections import deque

def solution(n, k, enemy):
    """
    Args:
        n (int) : 준호가 갖고 있는 병사 수
        k (int) : 무적권 스킬 사용 가능 횟수
        enemy (List) : 매 라운드마다 공격해오는 적의 수
    Returns:
        최대한 준호가 막을 수 있는 라운드 수
    """
    answer = 0
    sorted_enemy = sorted(enemy, reverse=True)[:k]
    queue = deque(enemy)
    
    while n > 0:
        if not queue:
            break

        e = queue.popleft()
        if k > 0 and e in sorted_enemy:
            k-= 1
            sorted_enemy.remove(e)
        else:
            if e > n:
                break
            n -= e
        answer += 1
        
    return answer


# ✅ 
# 큰 것만 스킬 써서 빼기 전에 우선 앞에서 n을 다 써버리면 소용이 없다.
# 이 부분을 고려해서 다시 풀어야 함 
import heapq

import heapq

def solution(n, k, enemy):
    """
    Args:
        n (int) : 준호가 갖고 있는 병사 수
        k (int) : 무적권 스킬 사용 가능 횟수
        enemy (List) : 매 라운드마다 공격해오는 적의 수
    Returns:
        최대한 준호가 막을 수 있는 라운드 수
    """
    heap = []
    accum_e = 0
    
    for i, e in enumerate(enemy):
        heapq.heappush(heap, -e)
        accum_e += e
        
        if accum_e > n:
            if k > 0:
                p = heapq.heappop(heap)
                accum_e += p
                k -= 1
            else:
                return i
            
    return len(enemy)

if __name__== "__main__":
    n = 7
    k = 3
    enemy = [4, 2, 4, 5, 3, 3, 1]

    # n=2
    # k=4
    # enemy = [3,3,3,3]

    print(solution(n, k, enemy))
