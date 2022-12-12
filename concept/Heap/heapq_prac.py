import heapq


# 파이썬의 heapq 모듈읜 최소힙으로 생성된다. 
heap = [] # 빈 리스트 선언

# heapq.heappush(heap, item): item을 heap에 추가
heapq.heappush(heap, 1000)
heapq.heappush(heap, 10)
heapq.heappush(heap, 100)

print(heap) # [10, 1000, 100]

# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
heapq.heappop(heap)

print(heap) # [100, 1000]

# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
heap2 = [200, 20, 100]

heapq.heapify(heap2) # [20, 200, 100]

# 최대 힙 만들기
heap = [1, 2, 3, 4, 5]
max_heap = []

for item in heap:
    heapq.heappush(max_heap, (-item, item))
print(max_heap) # [(-5, 5), (-4, 4), (-2, 2), (-1, 1), (-3, 3)], 튜플 형태의 힙 구조

max_value = heapq.heappop(max_heap)
print(max_value[1]) # 5 (최댓값 반환)