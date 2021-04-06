# 동규가 할 수 있는 최적의 무브를 찾아 움직이는 함수
def move(current):
    min_dist = abs(current-M)
    if current < M:
        if abs((current * A)-M) < min_dist:
            min_dist = abs((current * A)-M)
            N = current * A
        if abs((current * B)-M) < min_dist:
            min_dist = abs((current * B)-M)
            N = current * B
        if abs((current + A)-M) < min_dist:
            min_dist = abs((current + A)-M)
            N = current + A
        if abs((current + B)-M) < min_dist:
            min_dist = abs((current + B)-M)
            N = current + B
        if abs((current + 1)-M) < min_dist:
            min_dist = abs((current + 1)-M)
            N = current + 1
    else:
        if abs((current - A)-M) < min_dist:
            min_dist = abs((current - A)-M)
            N = current - A
        if abs((current - B)-M) < min_dist:
            min_dist = abs((current - B)-M)
            N = current - B
        if abs((current - 1)-M) < min_dist:
            min_dist = abs((current - 1)-M)
            N = current - 1
    return N

A, B, N, M = map(int, input().split())


ans = 0
# 동규의 위치가 주미랑 같아질때까지 계속 반복
while N != M:
    ans += 1
    N = move(N)

print(ans)