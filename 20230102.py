def solution(lines):
    
    def convert_time(time):
        return (int(time[0:2]) * 60 * 60 + int(time[3:5]) * 60 + int(time[6:8])) * 1000 + int(time[9:])
        
        
            
    def get_starttime(t1, s):
        hour, minute, second = t1.split(':')
        time = convert_time(t1)
        
        sec = 0
        if '.' in s:
            sec = int(s.split('.')[0])* 1000 + int(s.split('.')[1][:-1])
        else:
            sec = 1000 * int(s[:-1])
        #print(hour, minute, second, time, sec, time-sec)
        
        return (time - sec +1)
        
        
    
    time_arr = []
    for line in lines:
        _, time, sec = line.split()
        start_time = get_starttime(time, sec)
        time = convert_time(time)
        time_arr.append([start_time, time])

    array = time_arr
    array.sort()
    #print(array)
    answer = 0
    
    max_cnt = 0
    for i in range(len(array)):
        cnt = 0
        target_time = array[i][0]-1000
        for j in range(i+1):
            if array[j][1] > target_time:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt

