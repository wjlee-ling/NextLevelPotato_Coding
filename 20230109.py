# A E I O U 만을 사용하여 만들 수 있는 길이 5 이하의 모든 단어 (A ~ UUUUU)

# 단어 사전 리스트를 구성
# 정렬
# 주어진 word에 대한 index를 찾는다.

from itertools import product

def solution(word):
    """
    Args:
        word (str) : 단어
    Returns:
        해당 단어가 몇 번째 단어인지 반환
    """
    dictionary = []
    words = ["A", "E", "I", "O", "U"]

    for i in range(1, len(words)+1):
        dictionary.extend(''.join(list(p)) for p in product(words, repeat=i))
        
    dictionary.sort()
    return dictionary.index(word) + 1