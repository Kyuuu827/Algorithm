# 프로그래머스_Lv4_징검다리
def solution(distance, rocks, n):
    answer = 0
    rocks.sort() # [2, 11, 14, 17, 21]
    rocks.append(distance)
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        current = 0
        target = float('inf') 
        rock_removed = 0

        for rock in rocks:
            dis = rock - current
            if mid > rock - current:
                rock_removed += 1
            else : 
                current = rock
                target = min(target, dis) 

        if rock_removed > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = target

    return answer

# 두 번째 풀이

print(solution(25, [2, 14, 11, 21, 17], 2))