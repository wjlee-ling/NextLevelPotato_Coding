"""
인풋을 보고 복잡도를 줄여야한다는건 알았는데
이것도 이분탐색..?
이분탐색을 하는 명확한 조건을 모르겠다. 그냥 시간복잡도 줄이러 무지성 이분탐색하는 느낌
"""

from collections import deque
import itertools
import heapq
import collections

def solution(stones, k):
    answer = 0
    stones = deque(stones)
    queue = deque()
    
    left = 0
    right = 2000000000
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for stone in stones:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0
            if count >= k:
                break
        if count < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer
    
 """
 sliding window로 하나씩 했다 => 당연히 시간초과
 """   

#     while idx + k <= len(stones):
#         #print(idx, stones[idx:idx+k])
#         if 
#         array.append(max(stones[idx:idx+k]))  
#         idx += 1
    
#     print(array)
#     answer = min(array)

 """
인터넷 코드를 참고하여 heap으로 구현 -> 시간초과
 """   

#     heap = list()
#     output = list()

#     for i in range(0, len(stones)):
#         while len(heap) and i-k >= heap[0][1]:
#             heapq.heappop(heap)
#         heapq.heappush(heap, (-stones[i], i))
#         if len(heap) >= k:
#             output.append(-1 * heap[0][0])


#     answer = min(output)

    
        
                
    
    
    
    return answer