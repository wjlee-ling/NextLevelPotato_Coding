# FAIL

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split()) # 방 개수, 복도 개수s
A_list = list(map(int, input().split())) # A1....,An
temp = [list(map(int, input().split())) for _ in range(M)]