# 프로그래머스_Lv2_더 맵게
# 1차 풀이 (오답)
def solution(scoville, K):
    count  = 0
    low = []

    while min(scoville) <= K:
        low.append(scoville.pop(scoville.index(min(scoville))))
        low.append(scoville.pop(scoville.index(min(scoville)))*2)
        scoville.append(sum(low))
        count += 1

    return count


# 2차 풀이(정확도 100%, but 효율성 테스트 실패)
import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    while scoville:
        if min(scoville) >= K:
            return count
        low = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, low)
        count += 1

        if len(scoville) < 2 and scoville[0] < K:
            return -1


# 3차 풀이(정확도, 효율성 테스트 통과)
import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        low = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, low)
        count += 1
        if len(scoville) < 2 and scoville[0] < K:
            return -1
    
    return count