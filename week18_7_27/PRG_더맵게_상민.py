import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        min_value = heapq.heappop(scoville)
        if min_value >= K:
            return answer
        if not len(scoville):
            return -1
        min_second_value = heapq.heappop(scoville) * 2
        new_value = min_value + min_second_value
        heapq.heappush(scoville, new_value)
        answer += 1
    return answer
