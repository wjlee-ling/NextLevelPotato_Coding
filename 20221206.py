# Programmers 12951: JadenCase 문자열 만들기


# JadenCase : 모든 단어의 첫 문자는 대문자, 나머지는 소문자
## 무조건 대문자로 변환하는 경우는 첫 문자여야 함

# 우선 문자열 띄어쓰기 기준 토크나이징
# loop을 돌면서 앞 글자가 알파벳이면 앞글자만 대문자로 변환하고 나머지는 다 소문자로 변환
## capitalize는 문자열의 첫글자는 대문자로 나머지는 소문자로 바꿔줌

def solution(s):
    """
    Args:
        s (str) : 주어지는 문자열
    Returns:
        주어진 문자열 s를 JadenCase로 바꾼 문자열로 반환
    """
    answer = []
    
    tokens = list(s.split(" "))
    for token in tokens:
        answer.append(token.capitalize())
    
    return " ".join(answer)