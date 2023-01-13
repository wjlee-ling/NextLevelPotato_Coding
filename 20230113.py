def solution(word):
    """
    n개의 모음으로 된 단어의 개수: 5*(n-1개의 모음으로 된 단어)
    """
    combn = {1:["A","E","I","O","U"], 2:[], 3:[], 4:[], 5:[]}
    i = 2
    while i < 6:
        for char in ["A", "E", "I", "O", "U"]:
            # combn[i].append(char+"X"*(i-1))
            for unit in combn[i-1]:
                combn[i].append(char+unit)
        i +=1
    sums = {k: len(v) for k,v in combn.items()}
    cumsums = {0:0}
    cumsum = 0
    for k,v in sums.items():
        cumsum += v
        cumsums[k] = cumsum
    # {1: 5, 2: 25, 3: 125, 4: 625, 5: 3125}
    # {1: 5, 2: 30, 3: 155, 4: 780, 5: 3905}
    char2num = {"A":0, "E":1, "I":2, "O":3, "U":4}
    answer = 0
    for p, char in enumerate(word, start=1):
        answer += char2num[char] * cumsums[5-p] + char2num[char] + 1
    
    return answer
