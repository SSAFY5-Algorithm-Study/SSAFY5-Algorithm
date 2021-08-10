
"""
K = 가지고 있는 랜선의 갯수
N = 만들어야 되는 랜선의 갯수
mid = 만들어야 되는 랜선의 각 길이
cnt = mid 길이 일때 만들 수 있는 랜선의 갯수
answer = 실제 가능한 랜선의 길이

접근법:
현재 만들려고 하는 랜선의 길이가 mid일때 랜선을 몇개 만들 수 있을까?
랜선을 N보다 많이 만들 수 있다 --> 랜선의 길이를 늘린다
                             --> answer에 값을 업데이트한다 (최적은 아니라도 일단 가능한 답이기 때문에) 
랜선을 N보다 적게 만들 수 있다 --> 랜선의 길이를 줄인다
"""
# import sys
# sys.stdin = open('input.txt', 'r')

K, N = map(int, input().split())

cables = [int(input()) for _ in range(K)]
left = 1
right = max(cables)
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for cable in cables:
        cnt += cable // mid
    
    if cnt >= N:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)