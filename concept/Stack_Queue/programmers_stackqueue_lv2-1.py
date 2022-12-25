# 프로그래머스_Lv2_기능개발
# Queue 문제다.
def solution(progresses, speeds):
    answer = []
    count = 0
    day = 0
    while len(progresses) > 0:
        day+=1
        if 100-(progresses[0] + day*speeds[0]) <= 0:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
            day-=1
        else:
            if count > 0:
                answer.append(count)
                count = 0
        
    answer.append(count)
    return answer

# collections 모듈 사용
from collections import deque


def solution(progresses, speeds):
    answer = []
    count = 0
    day = 0
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        day+=1
        if (progresses[0] + speeds[0]*day) >= 100:
            count+=1
            progresses.popleft()
            speeds.popleft()
            day-=1
        else:
            if count > 0:
                answer.append(count)
                count = 0
    
    answer.append(count)        
    return answer