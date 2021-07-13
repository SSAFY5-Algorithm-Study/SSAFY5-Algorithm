# 이분 탐색 이용...?

def check(mid, stones, k):
    cnt = 0
    for s in stones:
        if s <= mid:
            cnt += 1
        else:
            cnt = 0
        # 모두 잘 건너지 못한 경우
        if cnt >= k:
            return False
    return True

def solution(stones, k):
    start, end = min(stones), max(stones)
    
    while start <= end:
        mid = (start + end) // 2
        
        if check(mid, stones, k):
            start = mid + 1
        else:
            end = mid -1
    
    return start