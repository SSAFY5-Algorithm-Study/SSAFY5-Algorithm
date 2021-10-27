from itertools import permutations as perm
import math

# def solution(k, dungeons):
#     answer = 0
    
#     for p in perm([i for i in range(len(dungeons))]):
#         cur, cnt = k, 0
        
#         for index in p:
#             a, b = dungeons[index]
            
#             if cur >= a:
#                 cur -= b
#                 cnt += 1
        
#         answer = max(answer, cnt)

#     return answer

# 좀 더 효율적으로....?
def solution(k, dungeons):
    # 가능한 순서 -- 첫번째의 최소 필요 피로도는 무조건 k(현재 피로도) 이상이어야함
    dungeons.sort(reverse=True)
    n = len(dungeons)
    cycle = math.factorial(n) // n
    base = 0

    for i in range(n):
        if dungeons[i][0] < k:
            break
        base = i
    
    nums = [i for i in range(n)]
    perms = list(perm(nums))[:cycle*(base+2)]
    max_cnt = 0
    for p in perms:
        cnt, cur = 0, k
        for i in p:
            if cur < dungeons[i][0]:
                break
            cnt += 1
            cur -= dungeons[i][1]
        max_cnt = max(max_cnt, cnt)
        
    return max_cnt