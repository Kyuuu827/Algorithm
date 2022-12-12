# 타겟 넘버_lv2
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(idx, result):
        if idx == n:
            if target == result:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])

    dfs(0, 0)

    return answer

print(solution([4,1,2,1], 4))