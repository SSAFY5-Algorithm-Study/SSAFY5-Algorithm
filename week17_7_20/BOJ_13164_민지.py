"""
접근법
1. 옆에 있는 원생과의 키 차이를 담은 배열을 만든다
2. 가장 키 차이가 많이 나는 원생을 기준으로 그룹을 나눈다
3. K개로 그룹을 나누려면 K-1개의 구분선을 그어야 되므로 배열에서 가장 큰 값 K-1개를 제거한다
"""
from heapq import heappush, nlargest

N, K = map(int, input().split())
children = list(map(int, input().split()))
deltas = [] # 옆에 있는 원생과의 키 차이를 담을 배열
cost = 0 # 전체 비용

for i in range(1, N):
    delta = children[i] - children[i-1]
    heappush(deltas, children[i]-children[i-1])
    cost += delta

# 키 차이가 가장 큰 구간 K-1 개를 찾아서 그룹을 나누어준다
# 그룹을 나누게 되면 그 구간을 이어주고 있었던 cost는 전체 cost에서 빠지게 된다
cost -= sum(nlargest(K-1, deltas))

print(cost)