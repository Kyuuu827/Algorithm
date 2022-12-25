# 반복문
def binary_search(list):
    left = 0
    right = len(list)-1

    # left가 right보다 작거나 같다면
    while(left<=right):
        mid = (left+right) // 2  # mid 값 계산
    if list[mid] == 10:
        return mid  # 정답일 경우 정답 반환
    elif list[mid] < 10:
        left = mid + 1  # 정답보다 작을 경우 left를 mid+1로 이동
    elif list[mid] > 10:
        right = mid -1  # 정답보다 클 경우 right를 mid-1로 이동

    return mid

# 재귀함수
def binary_search_recursion(target, start, end, list):
    if start > end:
        return None

    mid = (start + end) // 2
    
    if list[mid] == target:
        return mid
    elif list[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
        
    return binary_search_recursion(target, start, end, list)