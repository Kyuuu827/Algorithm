# 짝 지어 제거하기_Lv2
# Stack으로 풀이
def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)
            
    if stack:
        return 0
    else:
        return 1