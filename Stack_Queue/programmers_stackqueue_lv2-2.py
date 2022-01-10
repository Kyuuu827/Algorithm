# 오답 풀이
def solution(priorities, location):
    complete = []
    myLocation = priorities[location]

    while len(priorities) > 0:
        if priorities[0] == max(priorities):
            complete.append(priorities.pop(0))

        else:
            priorities.append(priorities.pop(0))

    return complete.index(myLocation) + 1 
    
print(solution([1, 1, 9, 1, 1, 1], 0))

# deque를 이용한 풀이
from collections import deque


def solution(priorities, location):
    answer = 0
    a = deque([(j, i) for i,j in enumerate(priorities)])

    while len(a):
        list = a.popleft()
        if a and max(a)[0] > list[0]:
            a.append(list)
        else:
            answer += 1
            if list[1] == location:
                break
    return answer

print(solution([1, 1, 9, 1, 1, 1, 10], 6))