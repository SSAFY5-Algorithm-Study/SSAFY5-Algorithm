import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b * 2))
        answer += 1
        
    if scoville[0] < K:
        return -1
    
    return answer