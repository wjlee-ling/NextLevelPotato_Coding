'''
A,E,I,O,U를 사용해서 길이 5 이하인 단어 모음집
A -> AA -> AAA.. -> UUUUU
word가 사전에서 몇 번째 단어인가
idea: 단어집을 구축하고 몇 번째인지 찾기
중복 순열(itertools product) 
'''
from itertools import product

def solution(word):        
    words = [] # 나올 수 있는 combination을 담는 list
    alphabet = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        tmp = list(product(alphabet,repeat=i))
        for i in tmp:
            tmp_word = ''.join(i)
            words.append(tmp_word)
    words.sort()
    return words.index(word) + 1
