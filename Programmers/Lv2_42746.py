#프로그래머스_Lv2_가장 큰 수
def solution(numbers):
    answer = ''
    '''
    str_num = []
    for number in numbers:
        str_num.append(str(number))
    '''
    str_num = list(map(str, numbers)) # 위의 주석처리 된 부분과 동일한 코드(map함수 사용)
    str_num.sort(key=lambda x : x * 3, reverse=True)
    answer = str(int("".join(str_num)))

    return answer

print(solution([6, 10, 11, 2]))
