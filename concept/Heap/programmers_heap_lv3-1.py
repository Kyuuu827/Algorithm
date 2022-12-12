# 프로그래머스_Lv3_디스크 컨트롤러
import heapq as hq

def solution(jobs):
    answer, now, seq = 0, 0, 0
    start = -1
    heap = []

    while len(jobs) > seq:
        for i in jobs:
            if start < i[0] <= now:
                hq.heappush(heap, [i[1], i[0]]) # 현 시점에서 처리 가능한 작업을 힙에 저장

        if len(heap) > 0: # 현재 처리중이 작업이 있는 경우
            cur_job = hq.heappop(heap)
            start = now
            now += cur_job[0]
            answer += now - cur_job[1] # 종료 시간까지의 시간 계산 값
            seq += 1
        else:
            now += 1

    return answer//len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))