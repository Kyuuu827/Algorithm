# 없는 숫자 더하기
def solution(numbers):
    answer = 0
    dic = {}
    for i in range(0, 10):
        dic[i] = 0
    for j in numbers:
        dic[j] = 1
    for key, val in dic.items():
        if val == 0:
            answer += key
    return answer