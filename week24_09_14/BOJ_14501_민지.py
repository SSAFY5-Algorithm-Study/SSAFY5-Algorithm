from heapq import heappush

N = int(input())
appointments = []

for start in range(1, N+1):
    time, price = map(int, input().split())
    end = start + time - 1
    if end <= N:
        # 끝나는 시간이 낮은(빠른) 순서대로 정렬되면서 appointments에 추가
        heappush(appointments, [end, start, price])

DP = [0] * (N+1)
for end, start, price in appointments:
    profit = max(DP[:start]) + price
    DP[end] = max(DP[end], profit)

print(max(DP))

