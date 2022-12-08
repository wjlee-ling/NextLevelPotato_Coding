'''
d보다 작은 k의 배수 (1사분면에서만)
idea: 어떻게 직선 내의 점
d^2 >= x^2 + y^2를 만족하는 x,y 구하기
y의 정확한 값을 구하는 게 아니라 "개수"를 구한다
'''
def solution(k, d):
    cnt = 0
    for i in range(0, d+1, k): # x값에 따라 가능한 y값 갯수 계산
        y = int((d*d-i*i)**(1/2))
        #print(i, " ", y)
        cnt += y//k +1
    return cnt
