'''
병사 n명. 매 라운드마다 적이 enemy[i]명
남은 병사 수가 현재 라운드의 적 수보다 적으면 게임 종료
무적권 사용하면 병사 사용 않고 라운드 이김(k번 사용 가능)

몇 라운드까지 막을 수 있는 지 return
enemy에서 큰 값을 차례로 무적권 사용 -> 그 때까지 못 가면?
'''
from heapq import heappush, heappop
def solution(n, k, enemy):
    answer = 0
    heap = [] # 힙에는 무족권을 쓸 경우를 담는다
    tmp = 0 # 싸운 적의 수
    
    for e in enemy:
        heappush(heap, -e) # 힙은 최솟값부터 pop하므로 -
        tmp += e
        if tmp > n: # 무족권을 써야 함
            if k == 0: # 무족권 다 씀
                break
            else: # 무족권 사용 가능
                tmp += heappop(heap) #음수값이 나오므로
                k -= 1
        #print(heap, tmp)
        answer += 1
                
    return answer