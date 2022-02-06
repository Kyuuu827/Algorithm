# 주차 요금 계산
import math


def timeToMinute(time):
    h, m= map(int, time.split(':'))
    return h * 60 + m

def solution(fees, records):
    answer = []
    dic = {}

    for r in records:
        time, number, record = r.split(" ")
        
        if number in dic:
            dic[number].append([timeToMinute(time), record])
        else:
            dic[number] = [[timeToMinute(time), record]]

    r_list = list(dic.items())
    r_list.sort(key=lambda x : x[0])

    for r in r_list:
        t = 0

        for i in r[1]:
            if i[1] == 'IN':
                t -= i[0]
            else:
                t += i[0]

        if r[1][-1][1] == 'IN':
            t += timeToMinute('23:59')
        print(t)
        if t <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append((fees[1]+(math.ceil((t-fees[0])/fees[2])) * fees[3]))

    return answer

print(solution([180, 5000, 10, 600], 
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", 
    "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    ))