# 문자열 압축_Lv2 
def solution(s):
    answer = 1000
    
    if len(s) == 1:
        return 1
    
    for n in range(1, len(s)//2 + 1):
        temp = s[:n]
        cnt = 1
        result = ''

        for i in range(n, len(s) + 1, n):
            if temp == s[i:n+i]:
                cnt += 1
            else:
                if cnt == 1:
                    result += temp
                else:
                    result += str(cnt) + temp
                cnt = 1
                temp = s[i:n+i]

        if cnt != 1:
            result += str(cnt) + temp
        else:
            result += temp

        answer = min(answer, len(result))

    return answer

print(solution('aabbaccc'))