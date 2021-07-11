
# 문제 이해가 안가네.
# 풀이 보고 품.
N,K = map(int,input().split())
naegoo = list(map(int,input().split()))
robot=[0]*N

cnt = 0
while(naegoo.count(0) < K):
    cnt += 1
    # 컨베이어 벨트 이동
    a = naegoo.pop()
    naegoo.insert(0,a)
    robot.pop()
    robot.insert(0,0)
    # 마지막꺼 내리기
    robot[N-1] = 0

    # 컨베이어 벨트에서 로봇 한칸 옮기기. 옮길 수 있다면.
    for i in range(N-2,0,-1):
        if robot[i] and naegoo[i+1] and not robot[i+1]:
            robot[i] = 0
            robot[i+1] = 1
            # 내구도는 0이 최하이다.
            naegoo[i+1] = max(0, naegoo[i+1] - 1)
    # 마지막꺼 내리기 (내리는 위치에 도착하면 즉시 내리므로)
    robot[N-1] = 0

    # 로봇 올리기.
    if naegoo[0] and not robot[0]:
        robot[0] = 1
        naegoo[0] = max(0, naegoo[0]-1)
print(cnt)