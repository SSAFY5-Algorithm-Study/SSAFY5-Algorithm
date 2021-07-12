"""
접근법: stones[0:k] 부터 시작해 한칸씩 오른쪽으로 이동하면서
해당 구역에서의 max값을 찾는다. --> 이 max 값은 해당 구역을 지나갈 수 있는 최대 인원
만약 해당 구역의 max값이(part_max) 현재 나온 max값보다 작을 경우 max값을 갱신한다

예를 들어
stones = [1, 2, 3, 1, 4], k = 3 일 경우
[1, 2, 3] --> max = 3, 3명 통과 가능
[2, 3, 1] --> max = 3, 3명 통과 가능
[3, 1, 4] --> max = 4, 4명 통과 가능

이 세가지의 지역 max 중에서 가장 작은 값인 3이 정답이 된다 (왜냐하면 일단 3명이 첫번째 구간을 지나가지 못하기 때문)

"""
def solution(stones, k):
    # part_max = 부분 max값
    # min_max = 부분 max값들 중 가장 작은 값
    min_max = part_max = max(stones[:k])
    for i in range(0, len(stones)-k):
        if part_max == stones[i]:
            part_max = max(stones[i+1:i+k+1])  
            if part_max < min_max:
                min_max = part_max
    return min_max