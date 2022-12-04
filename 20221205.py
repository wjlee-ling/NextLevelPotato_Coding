# Programmers 12939: 최댓값과 최솟값 

# 공백을 기준으로 문자열을 분리하여 리스트에 저장
# 최소값 최대값을 추출하여 문제가 원하는 형태로 반환


def solution(s):
    """
    Args:
        s (str) : 공백으로 구분된 숫자 문자열
    Returns:
        "(최소값) (최대값)"형태의 문자열을 반환
    """
    answer = ''

    num_list = list(map(int, s.split(" ")))
    max_num = max(num_list)
    min_num = min(num_list)

    return f"{str(min_num)} {str(max_num)}"