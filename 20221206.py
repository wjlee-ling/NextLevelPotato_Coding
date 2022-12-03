def solution(s):
    # 공백을 기준으로 맨 앞글자 대문자
    s_list = s.split(' ')
    answer = []
    for s in s_list:
        if s == "": #issue: 공백 여러 개일 때 어떻게 처리
            answer.append('')
        else:
            answer.append(s.capitalize())
    return ' '.join(answer)