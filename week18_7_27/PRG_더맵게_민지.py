from heapq import heapify, heappop, heappush

def solution(scoville, K):
    heapify(scoville)
    
    cnt = 0
    while scoville[0] < K:
        # 만약 재료가 2개 미만으로 남았다면 -1를 리턴하고 break
        if len(scoville) < 2:
            cnt = -1
            break
        
        # 아니라면 두개의 재료를 뽑아서 섞기
        a, b = heappop(scoville), heappop(scoville)
        heappush(scoville, a + b*2)
        cnt += 1
        
    return cnt