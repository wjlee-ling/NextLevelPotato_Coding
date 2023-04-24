## 정답: https://velog.io/@mmzz0219/BOJ-5373-%ED%81%90%EB%B9%99-Python-JAVA

from collections import defaultdict
from copy import deepcopy

def init():
    graph = defaultdict(list)
    for side, color in zip(["U", "D", "F", "B", "L", "R"], ["w", "y", "r", "o", "g", "b"]):
        for _ in range(3):
            graph[side].append([color]*3)
    return graph
# U + : [R,F,L,B] 1행 , D+: [R,F,L,B] 3행, 
# F: [U] 3행,  L:3열, D: 1행 [R]: 1열,  B: [U] 1행, L:1열, [D]:3행, [R]:3열 
# R: [U]: 3열, B: 1열, D: 3열, F:3열, L: [U] 1열, [F] 1열, [D] 1열, [B] 3열
    
def rotate(graph, side, wise):
    if side == "U":
        order = ["F", "R", "B", "L"]
        xrange,yrange = [(0,0)]*4, [(0,2)]*4      
    elif side == "D":
        order = ["F", "R", "B", "L"]
        xrange, yrange = [(2,2)]*4, [(0,2)]*4
    elif side == "F":
        order = ["U", "R", "D", "L"]
        xrange, yrange = [(2,2), (0,2), (0,0), (0,2)], [(0,2), (0,0), (0,2), (2,2)] #
    elif side == "B":
        order = ["U", "L", "D", "R"]
        xrange, yrange = [(0,0), (0,2), (2,2), (0,2)], [(0,2),(0,0),(0,2),(2,2)]
    elif side == "L":
        order = ["U", "F", "D", "B"]
        xrange, yrange = [(0,2), (0,2), (0,2), (0,2)], [(0,0), (0,0), (0,0), (2,2)]
    elif side == "R":
        order = ["U", "B", "D", "F"]
        xrange, yrange = [(0,2), (0,2), (0,2), (0,2)], [(2,2), (0,0), (2,2), (2,2)]
    temp = deepcopy(graph)
    for idx, xs,ys in zip(range(4), xrange, yrange): # e.g. U, F, R
        for x in range(xs[0], xs[1]+1): 
            for y in range(ys[0], ys[1]+1):
                newidx = (idx+1) % 4 if wise == "+" else (idx-1) % 4
                if wise == "-" and idx == 0:
                    newidx = 3                   
                for nx in range(xrange[newidx][0], xrange[newidx][1]+1):
                    for ny in range(yrange[newidx][0], yrange[newidx][1]+1):
                        graph[order[newidx]][nx][ny] = temp[order[idx]][x][y]
    print(graph)
                        
n = int(input())
for _ in range(n):
    _ = input()
    graph = init()
    ls = input().split()
    for s in list(ls):
        rotate(graph, s[0], s[1])
    for idx in range(3):    
        print("".join(graph["U"][idx])) 
                        
        