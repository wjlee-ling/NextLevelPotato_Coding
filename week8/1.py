# 구름 숫자 표를 dict으로 만들기
# 두 글자 씩 자르면서 dict에 있으면 숫자 추가

import sys

def input():
    return sys.stdin.readline().rstrip()
answer = ""
goorm_dict = {"qw": 1, "as": 2, "zx": 3, "we": 4, "sd": 5, "xc": 6, "er": 7, "df": 8, "cv": 9, "ze": 0}

# 첫째 줄 입력 : 문자열의 길이
N = int(input())
# 둘째 줄 입력 : 구름 숫자로 표기한 숫자
goorm = input()

for i in range(len(goorm)-1):
	check = goorm[i:i+2]
	if check in goorm_dict:
		answer += str(goorm_dict[check])
	
print(answer)