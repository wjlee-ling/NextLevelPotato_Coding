# 구슬 탈출 2 https://www.acmicpc.net/problem/13460
# 삼성 구현

from collections import namedtuple
from copy import deepcopy

Ball = namedtuple("Ball", "x y color")
N, M = map(int, input().split())
graph = []
ans = float("inf")

for i in range(N):
    row = input()
    graph.append(row)
    for j in range(len(row)):
        if row[j] == "B":
            blue = Ball(i,j, "blue")
        elif row[j] == "R":
            red = Ball(i,j, "red")
        elif row[j] == "O":
            hole = Ball(i,j, "hole")

xmoves = [0,0,-1,1] # 좌, 우, 상, 하
ymoves = [-1,1,0,0]
dir_mapping = {0:"좌", 1:"우", 2:"상", 3:"하"}

def isValid(x, y, color):
    global red, blue, hole
    if (x < 0 or x >= N or y < 0 or y >=M):
        return False
    if graph[x][y] == "#" :
        return False
    if color == "blue" and x == red.x and y == red.y and (x,y) != (hole.x, hole.y):
        # 가는 방향에 다른 색 구슬이 있음
        # 다만 hole에 다른 색 구슬이 있었다면 이미 빠져서 없어졌음
        return False
    if color == "red" and x == blue.x and y == blue.y and (x,y) != (hole.x, hole.y):
        return False

    return True

def roll(dir, ball):
    # 구슬을 갈 수 있을 때까지 한칸 한칸 움직임
    dx, dy = xmoves[dir], ymoves[dir]
    cx, cy = ball.x, ball.y
    nx, ny = cx+dx, cy+dy
    while isValid(nx, ny, ball.color):
        cx, cy = nx, ny
        nx, ny = nx+dx, ny+dy
        if cx == hole.x and cy == hole.y:
            break
    
    return cx, cy

def roll_in_order(dir, first, second):
    global red, blue
    # first 공 돌리고 second 공 돌리기
    fx, fy = roll(dir, first)
    if first.color == "red":
        red = first._replace(x=fx, y=fy)
    else:
        blue = first._replace(x=fx, y=fy)

    sx, sy = roll(dir, second)
    if second.color == "red":
        red = second._replace(x=sx, y=sy)
    else:
        blue = second._replace(x=sx, y=sy)
    # return red, blue

def tilt(dir):
    global red, blue
    if dir == 0 and blue.x == red.x:
        # 좌로
        if blue.y < red.y:
            # 블루가 먼저
            first = blue
        else:
            first = red
    elif dir == 1 and blue.x == red.x:
        # 우로
        if blue.y < red.y:
            first = red
        else: 
            first = blue
    elif dir == 2 and blue.y == red.y:
        # 상
        if blue.x < red.x:
            first = blue
        else:
            first = red
    elif dir == 3 and blue.y == red.y:
        if blue.x < red.y:
            first = red
        else:
            first = blue
    else:
        first = blue
    second = blue if first == red else red
    # print(f"roling in order: {first.color} => {second.color}")
    roll_in_order(dir, first, second)
    # return red, blue

def step(cnt, prev_dir=None):
    global ans, red, blue, hole
    # 이전 dir가 '좌'이면 이번에도 '좌'나 '우'로는 기울 필요가 없음
    directions = [0,1,2,3]
    if prev_dir in directions:
        directions.remove(prev_dir)

    if cnt >= ans:
        return 
    
    # if cnt >= 11:
    #     ans = min(ans, 11)
    #     return 

    old_blue = deepcopy(blue)
    old_red = deepcopy(red)
    cnt += 1
    for dir in directions:
        tilt(dir)
        # print(f"cnt: {cnt} new dir: {dir_mapping[dir]} blue: {old_blue} => {blue} red: {old_red} => {red}")

        if blue.x == hole.x and blue.y == hole.y:
            # do not keep on going this way
            # backtracking
            blue = old_blue
            red = old_red            
            continue

        if red.x == hole.x and red.y == hole.y:
            ans = min(ans, cnt)
            return ;
        
        if cnt >= 11:
            return ;
    
        step(cnt, dir) 

        # backtracking
        blue = old_blue
        red = old_red

step(0)
if ans >= 11:
    ans = -1
print(ans)