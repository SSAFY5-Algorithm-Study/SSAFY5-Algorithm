# 2019 카카오 개발자 겨울 인턴십 : 징검다리 건너기

def solution(stones, k):
    left, right = 1, 200000000

    while left < right:
        center = (left+right) // 2
        no_pass = 0
        for stone in stones:
            if stone-center <= 0:
                no_pass += 1
            else:
                no_pass = 0
            if no_pass >= k:
                right = center
                break
        else:
            left = center + 1

    return left