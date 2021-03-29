N = int(input())
K = int(input())

# 센서들의 위치 (중복 제거, 오름차순 정렬)
sensors = list(set(map(int, input().split())))
sensors.sort()

# 센서들간의 거리를 저장할 리스트
sensors_dist = []
for i in range(len(sensors)-1):
    sensors_dist.append(sensors[i+1]-sensors[i])

sensors_dist.sort()

# 가장 긴 연결고리를 끊으면서 k-1개의 집중국 건설
# 만약 K == N이라면, 매 센서마다 집중국이 있는것이므로 거리는 0
if K < N:
    for _ in range(K-1):
        sensors_dist.pop()
    print(sum(sensors_dist))
else:
    print(0)