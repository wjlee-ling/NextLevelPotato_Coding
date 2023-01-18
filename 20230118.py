# 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화

# 귤 배열에서의 원소의 개수를 담은 딕셔너리를 구성
# 딕셔너리 key 값이 큰 것 부터해서 k에서 빼는 과정을 통해 results를 찾기

from collections import defaultdict

def solution(k, tangerine):
    """
    Args:
        k (int) : 한 상자에 담으려는 귤의 개수
        tangerine (List) : 귤의 크기를 담은 배열
    Returns:
        귤 k 개를 고를 때 크기가 서로 다른 종류의 수의 최솟값
    """
    answer = 0
    
    # 종류 별 개수 딕셔너리
    tang_dict = defaultdict(int)
    for t in tangerine:
        tang_dict[t] += 1
    
    # value 값을 기준으로 정렬
    tang_dict = sorted(tang_dict.items(), key = lambda item: item[1], reverse=True) # (종류, 개수)
    
    # k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값 찾기
    while k:
        for key, val in tang_dict:
            k -= val
            answer += 1
            if k <= 0:
                return answer