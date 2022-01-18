# 프로그래머스_Lv3_입국심사
def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        customer = 0
        for i in times:
            customer += mid // i

        if customer >= n:
            answer = mid
            right = mid -1

        elif customer < n:
            left = mid + 1

    return answer

print(solution(6, [7, 10]))