"""solved"""


def solution(lines):
    answer = 1

    times = []
    for line in lines:
        sec = make_second(line.split()[1])  # 초 단위로 환산
        time = float(line.split()[2][:-1])  # 소수점 초

        start = sec - (time * 1000 - 1)
        times.append([start, sec])

    print(times)

    for i in range(len(times)):
        cnt = 0
        for j in range(i, len(times)):
            if times[i][1] > times[j][0] - 1000:
                cnt += 1
        answer = max(answer, cnt)

    return answer


def make_second(time):
    # print(time)
    t = list(map(float, time.split(":")))
    result = (t[0] * 3600 + t[1] * 60 + t[2]) * 1000
    return result


if __name__ == "__main__":
    lines = [
        ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"],
        ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"],
        [
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s",
        ],
    ]
    result = [1, 2, 7]

    for line in lines:
        print(solution(line))
