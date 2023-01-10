import heapq

def solution(n, k, enemy):
    answer = 0
    array = [] 
    count = 0
    for i in range(len(enemy)):
        heapq.heappush(array, (-enemy[i], enemy[i]))
        count += enemy[i]
        if count > n: 
            if k == 0:
                break
            else:
                count += heapq.heappop(array)[0]
                k -= 1

        answer += 1
    #print(array)
    
    return answer
