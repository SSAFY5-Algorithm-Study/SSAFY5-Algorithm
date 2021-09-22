from heapq import heappush

N = int(input())
appointments = []

for start in range(1, N+1):
    time, price = map(int, input().split())
    end = start + time - 1
    if end <= N:
        # 끝나는 시간이 낮은(빠른) 순서대로 정렬되면서 appointments에 추가
        heappush(appointments, [end, start, price])

# DP[i] = 현재 시점에서 만들 수 있는 최대 수익
# (일이 끝나는 지점 기준 => 아직 진행중인 일은 수익 창출 X)
DP = [0] * (N+1)
for end, start, price in appointments:
    # profit = 현재 일을 한다고 가정했을때 나올 수 있는 최대 수익
    # 현재 시작점 보다 빨리 끝나는 것들 중에서 최대 수익을 내는 것 + 현재 가격
    profit = max(DP[:start]) + price
    # DP 배열 값을 업데이트
    DP[end] = max(DP[end], profit)

print(max(DP))

