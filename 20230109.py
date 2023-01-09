# 괄호와 사칙연산만 사용가능
# 나누기 연산에서 나머지는 무시

# 'N' 1개로 만들 수 있는 숫자 => N
# 'N' 2개로 만들 수 있는 숫자 => NN / (N+N), (N-N), (N//N), (N*N) : 이전 'N' 1개로 만들 수 있는 숫자를 가지고 사칙연산
# 'N' 3개로 만들 수 있는 숫자 => NNN / 이전 실행 결과들로 사칙연산 조합해서 만들 수 있음

def solution(N, number):
    """
    Args:
        N (int) : 사용할 숫자
        number (int) : 만들어야 할 숫자
    Returns:
        N과 사칙연산만 사용해서 숫자를 표현할 때 N 사용횟수의 최솟값
    """
    answer = -1
    DP = []

    for i in range(1, 9): # 최솟값이 8보다 크면 -1 반환
        numbers = {int(str(N)*i)}
        
        for j in range(0, i-1):
            for x in DP[j]:
                for y in DP[-j-1]:
                    numbers.add(x+y)
                    numbers.add(x-y)
                    numbers.add(x*y)
                    if y != 0:
                        numbers.add(x//y)

        if number in numbers:
            return i

        DP.append(numbers)

    return answer