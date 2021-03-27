import heapq as hq

"""
접근법: 무조건 현재 상황에서 가장 작은 두 수를 더하는 것이
최종 카드의 합을 적게 만드는 방법이다

힙 정렬 활용: 파이썬의 heapq 라이브러리를 활용하면 쉽게 사용할 수 있다
힙 정렬을 사용하면 전체 리스트가 정렬 되지는 않지만, max나 min값만 반복해서 사용해야 할 경우
작은 시간 복잡도로 사용할 수 있는 정렬 방법
https://leedakyeong.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%ED%9E%99-%EC%A0%95%EB%A0%AC-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-heap-sort-in-python

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