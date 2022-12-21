ing korean
N = int(input())
data = list(input())
dict = {}
dict['ze'] = 0
dict['qw'] = 1
dict['as'] = 2
dict['zx'] = 3
dict['we'] = 4
dict['sd'] = 5
dict['xc'] = 6
dict['er'] = 7
dict['df'] = 8
dict['cv'] = 9

answer = ''
for i in range(N-1):
        now = data[i] + data[i+1]
            if now in dict.keys():
                        answer += str(dict[now])
                        print(answer)
                            
                                
