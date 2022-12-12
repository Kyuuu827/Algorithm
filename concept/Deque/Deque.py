from collections import deque

deq = deque()

# 덱의 가장 왼쪽 끝에 삽입
deq.appendleft(3)

# 덱의 가장 끝에 요소 삽인
deq.append(10)

# 가장 끝의 요소를 가져오면서 덱에서 삭제
deq.pop()

# 가장 왼쪽 요소를 가져오면서 덱에서 삭제
deq.popleft()

# 주어진 배열을 순환하면서 덱의 오른쪽에 추가
deq.extend([1, 2, 3])

# 주어진 배열을 순환하면서 덱의 왼쪽에 추가 
deq.extendleft([1, 2, 3]) # 결과적으로 [3, 2, 1] 순으로 추가 됨

# 엘리먼트를 데크에서 찾아 삭제
deq.remove(1) # 현재 deque 객체에 요소 1 이 두개가 있으나 앞에 있는 1만 삭제 된다. 

# 내용 반전
deq.reverse()

# 데크를 num만큼 회전(양수면 오른쪽, 음수면 왼쪽)
deq.rotate(1) # 오른쪽으로 한 칸씩 이동(맨 뒤의 요소가 맨 앞으로 이동)
deq.rotate(-1) # 왼쪽으로 한 칸씩 이동(맨 앞의 요소가 맨 뒤로 이동)
