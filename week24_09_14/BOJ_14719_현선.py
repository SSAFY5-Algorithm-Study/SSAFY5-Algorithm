h,w = map(int, input().split())

blocks = list(map(int, input().split()))

# 체크하려고
arr = [[0] * w for _ in range(h)]

# 땅이 있는 부분 1로 만들기
for i in range(w):
    k = blocks[i]
    if k > 0:
        for j in range(k):
            arr[j][i] = 1

total = 0
# arr 처음부터 다 돌면서
for i in range(h):
    k = 0
    for j in range(1, w):
        # 만약 이번에 도착한 곳이 땅인데 이전에 도착한 곳도 땅이면 k = 0
        if arr[i][j-1] == 1 and arr[i][j] == 1:
            k = 0
        # 이번에 도착한 곳이 빈 공간인데 지난번에 땅이었으면 카운팅
        elif k == 0 and arr[i][j-1] == 1:
            k += 1
        # 이번에 도착한 곳이 빈 공간인데 물이 고이는 중이면 계속 카운트
        elif k != 0 and arr[i][j] == 0:
            k += 1
        # 물이 고이다가 새로운 땅을 만나면 지금까지 고인 물들 더해줌
        elif k != 0 and arr[i][j] == 1:
            total += k
            k = 0
print(total)