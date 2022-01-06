#프로그래머스 Lv2_피보나치 수 
# 피보나치 수 : 0 1 1 2 3 5 8 13...

# 1. 재귀를 사용한 코드
def solution(n):
    if n < 2:
        return n
    else:
        return (solution(n-2) + solution(n-1)) % 1234567

#2. Iteration을 사용한 코드
def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a % 1234567
