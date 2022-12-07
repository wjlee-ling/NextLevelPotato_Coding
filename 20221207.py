#from itertools import permutations
#from itertools import product

def solution(n, times):
    answer = 0
    times.sort()
    
    left = 0
    right = n * times[-1]
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        
        for i in times:
            count += mid // i
            if count >= n:
                break
        
        if count >= n:
            answer = mid
            right = mid - 1
        elif count < n:
            left = mid + 1
        # if(left == right-1):
        #     answer = right
        #     break
    print(count)
    
    
    return answer


#     start = 0
#     end = n * times[-1]
    
#     while start < end:
#         mid = (start + end) // 2
#         total = 0
#         for time in times:
#             total += mid // time

#         if total >= n:
#             end = mid
#         else:
#             start = mid + 1
#     answer = start
    
#     return answer