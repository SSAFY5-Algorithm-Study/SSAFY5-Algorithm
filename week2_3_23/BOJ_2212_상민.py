# 서로 연결되어 있는 센서간 거리를 구한다.
# 그리고 최소 거리를 구해야하니 거리중에서 가장 긴 거리를 빼준다 (k만큼)


def get_ans(K, N):
    # 수신기가 센서보다 많으면 무조건 거리는 0이다.
    if K >= N:
        return 0
    for i in range(1, len(sensors)):
        distances.append(sensors[i] - sensors[i - 1])
    distances.sort()
    # 첫 번째 수신기는 첫 번째 센서에 설치한다
    # 그리고 최소값을 구하려면 제일 긴 거리의 연결고리를 끊어줘야 하기 때문에 그 거리의
    # 를 끊어준다
    for _ in range(K - 1):
        distances.pop()
    return sum(distances)


N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split())))
distances = []

print(get_ans(K, N))





