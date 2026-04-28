from heapq import heapify, heappop, heappush
def solution(scoville, K):
    
    heapify(scoville) # min heap
    cnt = 0
    while(len(scoville) >= 2):
        # min 값이 K 이상이라면 cnt 반환
        if scoville[0] >= K:
            return cnt
        # pop, mix and push 
        mixed = heappop(scoville) + heappop(scoville) * 2
        heappush(scoville, mixed)
        cnt += 1
    
    if scoville[0] >= K:
        return cnt
    else:
        return -1