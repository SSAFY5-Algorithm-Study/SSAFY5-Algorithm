import heapq as hq

"""
접근법: 무조건 현재 상황에서 가장 작은 두 수를 더하는 것이
최종 카드의 합을 적게 만드는 방법이다
"""
n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 힙정렬을 하기 위해 list 세팅하기
hq.heapify(cards)

for _ in range(m):
    # 가장작은 두개의 값의 합 구하기
    temp = hq.heappop(cards) + hq.heappop(cards)
    # 두개의 합을 구해 다시 리스트에 넣기
    hq.heappush(cards, temp)
    hq.heappush(cards, temp)

print(sum(cards))