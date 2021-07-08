"""
접근법
1. 내구도를 담은 배열과 로봇의 위치를 담은 배열 두개를 만들어서 기록하자
2. 디버깅 할때 편하게 각 과정을 함수화 시켜서 만들자
"""
from collections import deque


def remove_robot():
    if robots[N-1]:
        robots[N-1] = 0

# 1. 벨트 회전
def move_belt():
    belt.rotate(1)
    robots.rotate(1)
    # 벨트 이동 후 내리는 자리에 있는 로봇이 있다면 내린다
    remove_robot()


# 2. 로봇 이동 + 추가
def move_robots():
    # 로봇 이동
    for i in range(N-2, 0, -1):
        if robots[i] == 1 and robots[i+1] == 0 and belt[i+1] >= 1:
            robots[i], robots[i+1] = 0, 1
            belt[i+1] -= 1

    # 로봇 추가
    if not robots[0] and belt[0] >= 1:
        robots[0] = 1
        belt[0] -= 1
    
    # 로봇 내리기
    remove_robot()

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0] * (2*N))
loop = 0

while belt.count(0) < K:
    move_belt()
    move_robots()
    loop += 1

print(loop)
